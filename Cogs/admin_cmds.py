# Coding=UTF8
# !python
# !/usr/bin/env python3

import discord
from discord.ext import commands
import asyncio, random
from lib import db
from discord_components import Button, ButtonStyle, DiscordComponents

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

            if check_guild_exists == True and chid !=0:
                db.execute("UPDATE adminsettings SET LogChannelID = ? WHERE GuildID = ?", chid, ctx.guild.id)
                db.commit()

            elif check_guild_exists == True and check_chid == 0:
                db.execute("UPDATE adminsettings SET LogChannelID = ? WHERE GuildID = ?", chid, ctx.guild.id)
                db.commit()

            logch = db.field("SELECT LogChannelID FROM adminsettings WHERE GuildID = ?", ctx.guild.id)
            await self.client.get_channel(logch).send(embed=discord.Embed(title="Log Channel created!", timestamp=ctx.message.created_at, color=discord.Color.dark_orange(), description = f"<#{logch}> has been set as `Log Channel`."))
        except Exception as e:
            print(e)
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

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        db.execute("DELETE FROM adminsettings WHERE GuildID = ?", guild.id)
        db.commit()
        print('removed guild from adminsettings table')


    @commands.is_owner()
    @commands.command()
    async def servers(self, ctx):
        activeservers = self.client.guilds
        for guild in activeservers:
            await ctx.send(guild.name)
            await ctx.channel.send(f"{guild.name} - {guild.owner}")

    @commands.command(name="verify")
    async def verify(self, ctx):
        check_guild_exists = db.cursor.execute("SELECT 1 FROM adminsettings WHERE GuildID = ?", (ctx.guild.id,))
        check_guild_exists = check_guild_exists.fetchone() is not None
        #print(check_guild_exists)
        check_verify = db.field("SELECT Verify FROM adminsettings WHERE GuildID = ?", ctx.guild.id)
        after_role = db.field("SELECT Roles FROM adminsettings WHERE GuildID = ?", ctx.guild.id)
        #print(check_verify)
        role = discord.utils.find(lambda r: r.name == after_role, ctx.message.guild.roles)
        check_verifych = db.field("SELECT VerifyChID FROM adminsettings WHERE GuildID = ?", ctx.guild.id)

        #print(type(check_verifych), type(ctx.channel.id))
        #print(check_verify)
        #print(check_guild_exists)
        if check_verify == 'true' and int(check_verifych) == ctx.channel.id and check_guild_exists == True and role not in ctx.author.roles:

            dict = {"apple": "🍎", "banana": "🍌", "meat": "🍗", "grapes": "🍇", "pineapple": "🍍", "airplane": "✈", "car": "🚕", "bird": "🐦", "penguin": "🐧", "horse": "🐴", "frog": "🐸", "hat": "👒"}
            keys  = random.sample(list(dict), 3)
            # print(keys)
            target = keys.index(keys[0])
            randbuttons = random.sample(list(keys), 3)
            #print(randbuttons)
            #print(keys[target])
            #print(target)

            content = [
                [
                    Button(style=ButtonStyle.grey, label=dict[randbuttons[0]], custom_id = randbuttons[0]),
                    Button(style=ButtonStyle.grey, label=dict[randbuttons[1]], custom_id = randbuttons[1]),
                    Button(style=ButtonStyle.grey, label=dict[randbuttons[2]], custom_id = randbuttons[2])
                    ]
                ]

            msg = await ctx.channel.send(f"Click on the {keys[0]} emoji to verify. You have 1 minute to do this!", components=content)

            while True:
                try:
                    interaction = await self.client.wait_for('button_click', timeout=60)

                except asyncio.TimeoutError:
                    for row in content:
                        row.disable_components()
                    return await msg.edit(components=content)

                if interaction.author.id != ctx.author.id:
                    print('non-user')
                    await interaction.respond(content='This is not your button to click')

                elif interaction.author.id == ctx.author.id and interaction.custom_id != keys[target]:
                    for row in content:
                        row.disable_components()
                    await msg.edit("User clicked on the wrong button!", components=content)
                    return await interaction.respond(content='<:hellno:871582891585437759> Wrong! Do `*verify` to try again.')

                elif interaction.author.id == ctx.author.id and interaction.custom_id == keys[target]:
                    for row in content:
                        row.disable_components()
                    await ctx.author.add_roles(role)
                    print('added role')
                    return await msg.edit(f"{ctx.author.mention} Welcome to **{ctx.guild.name}**!", components=content)

        elif check_verify == 'false' or check_guild_exists == False:
            await ctx.reply("<:pandacop:831800704372178944> You cannot run this command since it is not set in the server!")

        elif role in ctx.author.roles:
            await ctx.reply("You are already Verified")
        elif int(check_verifych) != ctx.channel.id:
            await ctx.reply(f"This command can only be run in <#{check_verifych}>")

    @commands.has_permissions(administrator=True)
    @commands.command(name="set_verify")
    async def set_verify(self, ctx, operation: str, role: discord.Role = None, channel: discord.TextChannel = 0):
        role = role.name if role != None else None
        #print(type(channel))
        if role != None:
            if operation.lower() == 'add' and channel != 0:
                #print('executed main')
                channel = channel if isinstance(channel, int) else channel.id
                check_guild_exists = db.cursor.execute("SELECT 1 FROM adminsettings WHERE GuildID = ?", (ctx.guild.id,))

                search_role = discord.utils.find(lambda r:r.name == role, ctx.guild.roles)
                print(search_role)
                check_guild_exists = check_guild_exists.fetchone() is not None
                guild_id_lists = [x.id for x in ctx.guild.text_channels]
                #print(check_guild_exists)
                #print(channel)
                if search_role in ctx.guild.roles:
                    #print('found')
                    if operation.lower() == 'add' and check_guild_exists == True and channel in guild_id_lists:
                        db.execute("UPDATE adminsettings SET Verify = ? WHERE GuildID = ?", "true", ctx.guild.id)
                        db.execute("UPDATE adminsettings SET VerifyChID = ? WHERE GuildID = ?", channel, ctx.guild.id)
                        db.execute("UPDATE adminsettings SET Roles = ? WHERE GuildID = ?", role, ctx.guild.id)
                        db.commit()
                        #print('add executed')
                        await ctx.reply(f"<:verify:910515823590912010> Verification System has been turned on for **{ctx.guild.name}** successfully!")
                    #elif channel not in guild_id_lists:
                        #print('channel not in this guild')

                    if operation.lower() == 'add' and check_guild_exists == False and channel in guild_id_lists:
                        db.execute('INSERT OR IGNORE INTO adminsettings(GuildID, Verify, VerifyChID, Roles) VALUES(?, ?, ?, ?)', ctx.guild.id, "true", channel, role)
                        db.commit()
                        await ctx.reply(f"<:verify:910515823590912010> Verification System has been turned on for **{ctx.guild.name}** successfully!")
                        #print('add #2 executed')
                    #elif channel not in guild_id_lists:
                        #print("channel not in this guild(#2)")
                else:
                    await ctx.reply(f"<:hellno:871582891585437759> Role, {role} Was Not Found!")

            elif operation.lower() == 'add' and channel == 0:
                embed = discord.Embed(title="<:hellno:871582891585437759> Missing Arguments",
                                      description="```ini\nMissing Argument: [channel]```",
                                      timestamp=ctx.message.created_at, color=discord.Color.dark_grey())
                await ctx.send(embed=embed)

        elif role == None and operation.lower() == 'add':
            await ctx.channel.send("Role cannot be empty!!")

        check_guild_exists = db.cursor.execute("SELECT 1 FROM adminsettings WHERE GuildID = ?", (ctx.guild.id,))
        check_guild_exists = check_guild_exists.fetchone() is not None

        if check_guild_exists:
            check_verify_state = db.field("SELECT Verify FROM adminsettings WHERE GuildID = ?", ctx.guild.id)
            #print(check_verify_state)

        if operation.lower() == 'delete' and check_guild_exists == True and check_verify_state != 'false':
            db.execute("UPDATE adminsettings SET Verify = ?, VerifyChID = ?, Roles = ? WHERE GuildID = ?", "false", None, None, ctx.guild.id)
            db.commit()
            #print('executed delete')
            await ctx.reply(f'<:salute:831807820118622258> Disabled verification for **{ctx.guild.name}**!')
            #print('executed add')
        elif operation.lower() == 'delete' and check_guild_exists == False:
            #print('cannot execute delete since no value is set.')
            await ctx.reply("<:hellno:871582891585437759> Cannot disable verify if it has never been set in the server!")

        elif operation.lower() == 'delete' and check_verify_state == 'false' and check_guild_exists == True:
            await ctx.reply("<:hellno:871582891585437759> Cannot disable verify more than once!")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        db.execute("DELETE FROM adminsettings WHERE GuildID = ?", guild.id)
        db.commit()
        print('removed guild from adminsettings table')

    # @commands.command(name='temp')
    # async def temp(self, ctx):
    #     #print(ctx.guild.roles.name)
    #     db.execute("ALTER TABLE adminsettings ADD COLUMN Verify")
    #     db.execute("ALTER TABLE adminsettings ADD COLUMN VerifyChID")
    #     db.execute("ALTER TABLE adminsettings ADD COLUMN Roles")
    #     db.commit()
    #     #search_role = discord.utils.find(lambda r:r.name == 'deez nutz', ctx.guild.roles)
    #     #await ctx.send(ctx.author.roles)
    #     #if search_role in ctx.guild.roles:
    #         #await ctx.channel.send('found')
    #     await ctx.channel.send("Executed temp")

    @set_verify.error
    async def set_verify_error_handling(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.channel.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Permissions", description="```prolog\nYou must have the Administrator permission to use that command!```", timestamp=ctx.message.created_at, color=discord.Color.blue()))

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Required Argument", description="```ini\nMake sure you have run the command providing the [option], [role] and the [channel] parameters correctly!```", timestamp=ctx.message.created_at, color=discord.Color.blue()))

    @set_log_channel.error
    async def setlogch_error_handling(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Permissions", description="```prolog\nYou must have the Manage Channels permission to use that command!```", timestamp=ctx.message.created_at, color=discord.Color.magenta()))

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Required Argument", description="```ini\nMake sure you have run the command providing the [channel-id] parameter correctly!```", timestamp=ctx.message.created_at, color=discord.Color.blue()))

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

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Required Argument", description="```ini\nMake sure you have run the command providing the [member(s)] parameter correctly!```", timestamp=ctx.message.created_at, color=discord.Color.blue()))

    @massban.error
    async def ban_error_handling(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Permissions", description="```prolog\nYou must have the Ban Members permission to use that command!```"), timestamp=ctx.message.created_at, color=discord.Color.greyple())
        if isinstance(error, commands.UserNotFound):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Member Not Found", description='```ini\nSorry, the [member] you provided does not exists in the server.```', timestamp=ctx.message.created_at, color=discord.Color.blurple()))

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Required Argument", description="```ini\nMake sure you have run the command providing the [member(s)] parameter correctly!```", timestamp=ctx.message.created_at, color=discord.Color.blue()))

    @massunban.error
    async def ban_error_handling(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759>  Missing Permissions", description='```prolog\nYou must have the Ban Members permission to use that command!```', timestamp=ctx.message.created_at, color=discord.Color.gold()))
        if isinstance(error, commands.UserNotFound):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Member Not Found", description='```ini\nSorry, the [member] you provided does not exists in the server.```', timestamp=ctx.message.created_at, color=discord.Color.blurple()))

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Required Argument", description="```ini\nMake sure you have run the command providing the [member(s)] parameter correctly!```", timestamp=ctx.message.created_at, color=discord.Color.blue()))

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

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Required Argument", description="```ini\nMake sure you have run the command providing the [member] and the [reason] parameters correctly!```", timestamp=ctx.message.created_at, color=discord.Color.blue()))


    @ban_user.error
    async def ban_error_handling(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Permissions", description="```prolog\nYou must have the Ban Members permission to use that command!```", timestamp=ctx.message.created_at, color=discord.Color.greyple()))
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Member Not Found", description='```ini\nSorry, the [member] you provided does not exists in the server.```', timestamp=ctx.message.created_at, color=discord.Color.blurple()))

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Required Argument", description="```ini\nMake sure you have run the command providing the [member] and the [reason] parameters correctly!```", timestamp=ctx.message.created_at, color=discord.Color.blue()))


    @unban_user.error
    async def ban_error_handling(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759>  Missing Permissions", description='```prolog\nYou must have the Ban Members permission to use that command!```', timestamp=ctx.message.created_at, color=discord.Color.gold()))

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Required Argument", description="```ini\nMake sure you have run the command providing the [member] parameter correctly!```", timestamp=ctx.message.created_at, color=discord.Color.blue()))

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
