import discord, asyncio
from discord.ext import commands
from lib import db

class MessageLogs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(administrator=True)
    @commands.command(name="set_msglog")
    async def set_message_logs(self, ctx, operation: str, channel: discord.TextChannel = 0):
        if operation.lower() == 'add' and channel != 0:
            #print('executed main')
            channel = channel if isinstance(channel, int) else channel.id
            check_guild_exists = db.cursor.execute("SELECT 1 FROM adminsettings WHERE GuildID = ?", (ctx.guild.id,))
            check_guild_exists = check_guild_exists.fetchone() is not None
            guild_id_lists = [x.id for x in ctx.guild.text_channels]
                #print(check_guild_exists)
                #print(channel)
                #print('found')
            if operation.lower() == 'add' and check_guild_exists == True and channel in guild_id_lists:
                db.execute("UPDATE adminsettings SET LogMsg = ? WHERE GuildID = ?", "true", ctx.guild.id)
                db.execute("UPDATE adminsettings SET LogMChID = ? WHERE GuildID = ?", channel, ctx.guild.id)
                db.commit()
                #print('add executed')
                await ctx.reply(f"<:verify:910515823590912010> Message Logging has been turned on for **{ctx.guild.name}** successfully!")
                #elif channel not in guild_id_lists:
                    #print('channel not in this guild')

            if operation.lower() == 'add' and check_guild_exists == False and channel in guild_id_lists:
                db.execute('INSERT OR IGNORE INTO adminsettings(GuildID, LogMsg, LogMChID) VALUES(?, ?, ?)', ctx.guild.id, "true", channel)
                db.commit()
                await ctx.reply(f"<:verify:910515823590912010> Message Logging has been turned on for **{ctx.guild.name}** successfully!")
                #print('add #2 executed')
                #elif channel not in guild_id_lists:
                #print("channel not in this guild(#2)")
        elif operation.lower() == 'add' and channel == 0:
            embed = discord.Embed(title="<:hellno:871582891585437759> Missing Arguments", description="```ini\nMissing Argument: [channel]```",
                                      timestamp=ctx.message.created_at, color=discord.Color.dark_grey())
            await ctx.send(embed=embed)

        check_guild_exists = db.cursor.execute("SELECT 1 FROM adminsettings WHERE GuildID = ?", (ctx.guild.id,))
        check_guild_exists = check_guild_exists.fetchone() is not None

        if check_guild_exists:
            check_msglog_state = db.field("SELECT LogMsg FROM adminsettings WHERE GuildID = ?", ctx.guild.id)
            #print(check_verify_state)

        if operation.lower() == 'delete' and check_guild_exists == True and check_msglog_state != 'false':
            db.execute("UPDATE adminsettings SET LogMsg = ?, LogMChID = ? WHERE GuildID = ?", "false", None, ctx.guild.id)
            db.commit()
            #print('executed delete')
            await ctx.reply(f'<:salute:831807820118622258> Disabled Message Logging for **{ctx.guild.name}**!')
            #print('executed add')
        elif operation.lower() == 'delete' and check_guild_exists == False:
            #print('cannot execute delete since no value is set.')
            await ctx.reply("<:hellno:871582891585437759> Cannot disable message logging if it has never been set in the server!")

        elif operation.lower() == 'delete' and check_msglog_state == 'false' and check_guild_exists == True:
            await ctx.reply("<:hellno:871582891585437759> Cannot disable message logging more than once!")


    @commands.Cog.listener()
    async def on_message_delete(self, message):
        check_LogMsg_state = db.field("SELECT LogMsg FROM adminsettings WHERE GuildID = ?", message.guild.id)
        get_channel = db.field("SELECT LogMChID FROM adminsettings WHERE GuildID = ?", message.guild.id)

        if check_LogMsg_state == 'true' and get_channel != 0:
            embed=discord.Embed(title=f"{message.author.name} Deleted A Message", timestamp=message.created_at, color=discord.Color.red(), description = f"{message.author.mention} Deleted a message in <#{message.channel.id}>.\nThe Message Deleted Was: `{message.content}`")
            embed.set_footer(text='Delta Δ is the fourth letter of the Greek Alphabet', icon_url=message.author.avatar_url)
            embed.set_thumbnail(url="https://pandorafms.com/blog/wp-content/uploads/2020/12/567-Logs_-qu%C3%A9-son-y-por-qu%C3%A9-monitorizarlos.jpg")
            await self.client.get_channel(get_channel).send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, message_before, message_after):
        check_LogMsg_state = db.field("SELECT LogMsg FROM adminsettings WHERE GuildID = ?", message_before.guild.id)
        get_channel = db.field("SELECT LogMChID FROM adminsettings WHERE GuildID = ?", message_before.guild.id)

        if check_LogMsg_state == 'true' and get_channel != 0:
            embed=discord.Embed(title=f"{message_before.author.name} Edited A Message", timestamp=message_before.created_at, color=0xFFD700, description = f"{message_before.author.mention} Edited a message in <#{message_before.channel.id}>.\n**Old Message**: `{message_before.content}`\n**New Message**: `{message_after.content}`")
            embed.set_footer(text='Delta Δ is the fourth letter of the Greek Alphabet', icon_url=message_before.author.avatar_url)
            embed.set_thumbnail(url="https://pandorafms.com/blog/wp-content/uploads/2020/12/567-Logs_-qu%C3%A9-son-y-por-qu%C3%A9-monitorizarlos.jpg")
            await self.client.get_channel(get_channel).send(embed=embed)


    @set_message_logs.error
    async def set_mesage_logs_error_handling(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Arguments",
                                               description="```ini\nMake sure you have run the command providing the [operation] and [channel] parameters correctly.```", timestamp=ctx.message.created_at, color=discord.Color.blurple()))

        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Permissions", description="```prolog\nYou must have the Administrator permission to use that command!```", timestamp=ctx.message.created_at, color=discord.Color.magenta()))

    # @commands.command(name="temp")
    # async def temp(self, ctx):
    #     db.execute("ALTER TABLE adminsettings ADD COLUMN LogMsg")
    #     db.execute("ALTER TABLE adminsettings ADD COLUMN LogMChID")
    #     db.commit()
    #     await ctx.channel.send("executed")


def setup(client):
    client.add_cog(MessageLogs(client))
