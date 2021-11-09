# Coding=UTF8
# !python
# !/usr/bin/env python3

import discord
from discord.ext import commands
import asyncio


class AdminCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(manage_messages=True)
    @commands.command(name="purge", aliases=['clear', 'delete'])
    async def delete_channel_messages(self, ctx, limit: int=10):
        
        logch = db.field("SELECT LogChannelID FROM adminsettings WHERE GuildID = ?", ctx.guild.id)
        await ctx.channel.purge(limit=limit + 1) 
        await ctx.channel.send(f"<:salute:831807820118622258> Purged `{limit}` messages!")
        await asyncio.sleep(2)
        await ctx.channel.purge(limit=1)

        if logch != 0:
            embed = discord.Embed(title="Log Message", timestamp=ctx.message.created_at, color=discord.Color.dark_orange(), 
                    description=f"{ctx.author.mention} used `purge` in <#{ctx.channel.id}> to delete {limit} messages.")
            embed.set_footer(text='Delta Δ is the fourth letter of the Greek Alphabet', icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url="https://pandorafms.com/blog/wp-content/uploads/2020/12/567-Logs_-qu%C3%A9-son-y-por-qu%C3%A9-monitorizarlos.jpg")
            await self.client.get_channel(logch).send(embed=embed)



    @commands.has_permissions(kick_members=True)
    @commands.command(name="kick")
    async def kick_user(self, ctx, member: discord.Member, reason=None):

        logch = db.field("SELECT LogChannelID FROM adminsettings WHERE GuildID = ?", ctx.guild.id)
        await member.kick(reason=reason)
        await ctx.message.delete()
        await ctx.channel.send(f"<:pandacop:831800704372178944> Kicked {member.mention} successfully!")
        
        if logch != 0:
            embed=discord.Embed(title="Log Message", timestamp=ctx.message.created_at, color=discord.Color.dark_orange(), description = f"{ctx.author.mention} used `kick` in <#{ctx.channel.id}> to **kick** {member.mention} because `{reason}`")
            embed.set_footer(text='Delta Δ is the fourth letter of the Greek Alphabet', icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url="https://pandorafms.com/blog/wp-content/uploads/2020/12/567-Logs_-qu%C3%A9-son-y-por-qu%C3%A9-monitorizarlos.jpg")
            await self.client.get_channel(logch).send(embed=embed)

    @commands.has_permissions(ban_members=True)
    @commands.command(name="ban")
    async def ban_user(self, ctx, member: discord.Member, reason=None):
        logch = db.field("SELECT LogChannelID FROM adminsettings WHERE GuildID = ?", ctx.guild.id)
        await member.ban()
        #await ctx.channel.purge(limit=1)
        await ctx.message.delete()
        await ctx.channel.send(f"<:pandacop:831800704372178944> Banned {member.mention} successfully!")

        if logch != 0:
            embed=discord.Embed(title="Log Message", timestamp=ctx.message.created_at, color=discord.Color.dark_orange(), description = f"{ctx.author.mention} used `ban` in <#{ctx.channel.id}> to **ban** {member.mention} because `{reason}`")
            embed.set_footer(text='Delta Δ is the fourth letter of the Greek Alphabet', icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url="https://pandorafms.com/blog/wp-content/uploads/2020/12/567-Logs_-qu%C3%A9-son-y-por-qu%C3%A9-monitorizarlos.jpg")
            await self.client.get_channel(logch).send(embed=embed)


    @commands.has_permissions(ban_members=True)
    @commands.command(name="unban")
    async def unban_user(self, ctx, *, member:discord.User):
        logch = db.field("SELECT LogChannelID FROM adminsettings WHERE GuildID = ?", ctx.guild.id)

        await ctx.guild.unban(member)
        await ctx.channel.purge(limit=1)
        await ctx.channel.send(f"<:pandacop:831800704372178944> Unbanned {member.mention} successfully!")

        if logch != 0:
            embed=discord.Embed(title="Log Message", timestamp=ctx.message.created_at, color=discord.Color.dark_orange(), description = f"{ctx.author.mention} used `unban` in <#{ctx.channel.id}> to **unban** {member.mention}.")
            embed.set_footer(text='Delta Δ is the fourth letter of the Greek Alphabet', icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url="https://pandorafms.com/blog/wp-content/uploads/2020/12/567-Logs_-qu%C3%A9-son-y-por-qu%C3%A9-monitorizarlos.jpg")
            await self.client.get_channel(logch).send(embed=embed)


    @commands.command(name="masskick")
    @commands.has_permissions(kick_members=True)
    async def masskick(self, ctx, *users: discord.User):
        #print(type(users))
        logch = db.field("SELECT LogChannelID FROM adminsettings WHERE GuildID = ?", ctx.guild.id)
        
        await asyncio.gather(*map(ctx.guild.kick, users))
        await ctx.channel.purge(limit=1)
        await ctx.channel.send(f"<:pandacop:831800704372178944> Kicked {len(users)} member/s successfully!")

        if logch != 0:
            embed=discord.Embed(title="Log Message", timestamp=ctx.message.created_at, color=discord.Color.dark_orange(), description = f"{ctx.author.mention} used `masskick` in <#{ctx.channel.id}> to **kick** `{len(users)}` member/s.")
            embed.set_footer(text='Delta Δ is the fourth letter of the Greek Alphabet', icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url="https://pandorafms.com/blog/wp-content/uploads/2020/12/567-Logs_-qu%C3%A9-son-y-por-qu%C3%A9-monitorizarlos.jpg")
            await self.client.get_channel(logch).send(embed=embed)



    @commands.command(name="massban")
    @commands.has_permissions(ban_members=True)
    async def massban(self, ctx, *users: discord.User):
        logch = db.field("SELECT LogChannelID FROM adminsettings WHERE GuildID = ?", ctx.guild.id)
        
        await asyncio.gather(*map(ctx.guild.ban, users))
        await ctx.channel.purge(limit=1)
        await ctx.channel.send(f"<:pandacop:831800704372178944> Banned {len(users)} member/s successfully!")

        if logch != 0:
            embed=discord.Embed(title="Log Message", timestamp=ctx.message.created_at, color=discord.Color.dark_orange(), description = f"{ctx.author.mention} used `massban` in <#{ctx.channel.id}> to **ban** `{len(users)}` member/s.")
            embed.set_footer(text='Delta Δ is the fourth letter of the Greek Alphabet', icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url="https://pandorafms.com/blog/wp-content/uploads/2020/12/567-Logs_-qu%C3%A9-son-y-por-qu%C3%A9-monitorizarlos.jpg")
            await self.client.get_channel(logch).send(embed=embed)



    @commands.command(name="massunban")
    @commands.has_permissions(ban_members=True)
    async def massunban(self, ctx, *users: discord.User):
        logch = db.field("SELECT LogChannelID FROM adminsettings WHERE GuildID = ?", ctx.guild.id)

        await asyncio.gather(*map(ctx.guild.unban, users))
        await ctx.channel.purge(limit=1)
        await ctx.channel.send(f"<:pandacop:831800704372178944> Unbanned {len(users)} member/s successfully!")

        if logch != 0:
            embed=discord.Embed(title="Log Message", timestamp=ctx.message.created_at, color=discord.Color.dark_orange(), description = f"{ctx.author.mention} used `massunban` in <#{ctx.channel.id}> to **unban** `{len(users)}` member/s.")
            embed.set_footer(text='Delta Δ is the fourth letter of the Greek Alphabet', icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url="https://pandorafms.com/blog/wp-content/uploads/2020/12/567-Logs_-qu%C3%A9-son-y-por-qu%C3%A9-monitorizarlos.jpg")
            await self.client.get_channel(logch).send(embed=embed)



    @commands.has_permissions(manage_channels=True)
    @commands.command(name='setlogch')
    async def set_log_channel(self, ctx, chid: int):
        try:
            check_chid = db.field("SELECT LogChannelID FROM adminsettings WHERE GuildID = ?", ctx.guild.id)
            check_guild_exists = db.cursor.execute("SELECT 1 FROM adminsettings WHERE GuildID = ? ", (ctx.guild.id,))
            check_guild_exists = check_guild_exists.fetchone() is not None
            if check_guild_exists == False and chid !=0:
                print(ctx.guild.id)
                db.execute("INSERT OR IGNORE INTO adminsettings(GuildID, LogChannelID) VALUES(?, ?)", ctx.guild.id, chid)
                db.commit()
                await ctx.channel.send(f"Log Channel successfully created at <#{chid}>")

            elif check_guild_exists == True and check_chid == 0:
                db.execute("UPDATE adminsettings SET LogChannelID = ? WHERE GuildID = ?", chid, ctx.guild.id)
                db.commit()

            logch = db.field("SELECT LogChannelID FROM adminsettings WHERE GuildID = ?", ctx.guild.id)
            await self.client.get_channel(logch).send(embed=discord.Embed(title="Log Channel created!", timestamp=ctx.message.created_at, color=discord.Color.dark_orange(), description = f"<#{logch}> has been set as `Log Channel`."))
        except Exception:
                await ctx.channel.send("Make sure the bot has permission to read/send messages in the log channel and also provide the ChannelID correctly. ID must be an int.")
    

    @commands.has_permissions(manage_channels=True)
    @commands.command(name='deletelogch')
    async def delete_log_channel(self, ctx):
        #try:
        check_guild_exists = db.cursor.execute("SELECT 1 FROM adminsettings WHERE GuildID = ?", (ctx.guild.id,))
        #print('got check_guild_exists')
        before_delete = db.field("SELECT LogChannelID FROM adminsettings WHERE GuildID = ?", ctx.guild.id)
        #print('got before_delete') 
        check_guild_exists = check_guild_exists.fetchone() is None
        #print('got check_guild_exists') 
        if check_guild_exists == True and before_delete !=0:
            #print('check done')
            db.execute("UPDATE adminsettings SET LogChannelID = ? WHERE GuildID = ?", 0, ctx.guild.id)
            #print('db.execute done')
            db.commit()
            #print('saved')
            await ctx.channel.send(f"Won't log messages in <#{before_delete}> anymore!")

    @set_log_channel.error 
    async def setlogch_error_handling(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Permissions", description="```prolog\nYou must have the Manage Channels permission to use that command!```", timestamp=ctx.message.created_at, color=discord.Color.magenta()))

    @delete_log_channel.error 
    async def deletelogch_error_handling(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Permissions", description="```prolog\nYou must have the Manage Channels permission to use that command!```", timestamp=ctx.message.created_at, color=discord.Color.magenta()))


    @masskick.error
    async def kick_error_handling(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Permissions", description="```prolog\nYou must have the Kick Members permission to use that command!```", timestamp=ctx.message.created_at, color=discord.Color.magenta()))
        if isinstance(error, commands.UserNotFound):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Member Not Found", description="```ini\nSorry, the [member] you provided does not exists in the server.```"))

    @massban.error
    async def ban_error_handling(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Permissions", description="```prolog\nYou must have the Ban Members permission to use that command!```"), timestamp=ctx.message.created_at, color=discord.Color.greyple())
        if isinstance(error, commands.UserNotFound):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Member Not Found", description='```ini\nSorry, the [member] you provided does not exists in the server.```', timestamp=ctx.message.created_at, color=discord.Color.blurple()))

    @massunban.error
    async def ban_error_handling(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759>  Missing Permissions", description='```prolog\nYou must have the Ban Members permission to use that command!```', timestamp=ctx.message.created_at, color=discord.Color.gold()))
        if isinstance(error, commands.UserNotFound):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Member Not Found", description='```ini\nSorry, the [member] you provided does not exists in the server.```', timestamp=ctx.message.created_at, color=discord.Color.blurple()))

    @delete_channel_messages.error
    async def purge_error_handling(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.channel.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Permissions", description="```prolog\nYou must have the Manage Messages permission to use that command!```", timestamp=ctx.message.created_at, color=discord.Color.blue()))

    @kick_user.error
    async def kick_error_handling(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Permissions", description="```prolog\nYou must have the Kick Members permission to use that command!```", timestamp=ctx.message.created_at, color=discord.Color.magenta()))

        if isinstance(error, commands.MemberNotFound):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Member Not Found", description="```ini\nSorry, the [member] you provided does not exists in the server.```"))

    @ban_user.error
    async def ban_error_handling(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Permissions", description="```prolog\nYou must have the Ban Members permission to use that command!```"), timestamp=ctx.message.created_at, color=discord.Color.greyple())
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Member Not Found", description='```ini\nSorry, the [member] you provided does not exists in the server.```', timestamp=ctx.message.created_at, color=discord.Color.blurple()))

    @unban_user.error
    async def ban_error_handling(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759>  Missing Permissions", description='```prolog\nYou must have the Ban Members permission to use that command!```', timestamp=ctx.message.created_at, color=discord.Color.gold()))

    
#     @commands.command(name="lockdown") 
#     @commands.has_guild_permissions(manage_channels=True)
#     @commands.bot_has_guild_permissions(manage_channels=True)
#     async def lockdown(self, ctx, channel:discord.TextChannel=None):
#         channel = channel or ctx.channel
#         if ctx.guild.default_role not in channel.overwrites:
#             overwrites = {ctx.guild.default_role : discord.PermissionOverwrite(send_messages=False)}
#             await channel.edit(overwrites=overwrites)
#             print('done #1')
#             await ctx.send(f"`{channel.name}` is on Lockdown!!!")
# 
#         elif channel.overwrites[ctx.guild.default_role].send_messages == True or channel.overwrites[ctx.guild.default_role].send_messages == None:
#             overwrites = channel.overwrites[ctx.guild.default_role]
#             overwrites.send_messages = False
#             await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
#             print('done #2')
#             await ctx.send(f"`{channel.name}` is on Lockdown!!!")
#             
# 
# 
# 
#     @commands.has_guild_permissions(manage_channels=True)
#     @commands.bot_has_guild_permissions(manage_channels=True)
#     @commands.command(name="unlock")
#     async def unlock(self, ctx):
#         await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
#         await ctx.send(ctx.channel.name + " has been unlocked.")
        
#     @lockdown.error
#     async def lockdown_error_handling(self, ctx, error):
#         if isinstance(error, commands.MissingPermissions):
#             await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Permissions", description="```prolog\nYou must have the Manage Channels permission to use that command!```", timestamp=ctx.message.created_at, color=discord.Color.dark_grey()))
# 
#     @unlock.error
#     async def unlock_error_handling(self, error, ctx):
#         if isinstance(error, commands.MissingPermissions):
#             await ctx.channel.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Permissions", description="```prolog\nYou must have the Manage Channels permission to use that command!", timestamp=ctx.message.created_at, color=discord.Color.dark_orange()))

def setup(client):
    client.add_cog(AdminCmds(client))
