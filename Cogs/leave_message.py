# Coding=UTF8
# !python
# !/usr/bin/env python3

import discord, aiohttp, io
from discord.ext import commands
from lib import db
from discord.ext.commands.errors import BadArgument


class LeaveMsg(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(manage_guild=True)
    @commands.command(name="set_leave")
    async def set_welcome_message(self, message, channel_id: int = 0):
        choice = "true"
        # Checks if the guild id exists in database or not

        guild_id = db.cursor.execute("SELECT 1 FROM leave WHERE GuildID = ? ",
                                     (message.guild.id,))

        guild_id_exists = guild_id.fetchone() is not None

        # Does a simple check to see if the guild id exists or not...if it doesn't, then raise error else insert data

        if guild_id_exists is False and channel_id == 0:
            await message.channel.send("⚒  Oops! You cannot switch leave message off unless u switch it on!")
        elif guild_id_exists is False and channel_id != 0:
            db.execute("INSERT OR IGNORE INTO leave(GuildID, ChannelID, Choice) VALUES(?,?,?)",
                       (message.guild.id),
                       (channel_id), (choice))
            db.commit()
            await message.channel.send("⚒  Switched on leave message!")

            # await message.channel.send(" Oops! `channel_id` must be an integer type value!")

    @commands.has_permissions(manage_guild=True)
    @commands.command(name="update_leave")
    async def update_welcome_message(self, message, choice: str = "false"):
        guild_id = db.cursor.execute("SELECT 1 FROM leave WHERE GuildID = ? ",
                                     (message.guild.id,))

        guild_id_exists = guild_id.fetchone() is not None

        if guild_id_exists is False:
            await message.channel.send("⚒  Oops! You have to set leave message first before using this command.")
        else:
            # Updates the database

            try:
                if guild_id_exists is True and choice == "false":
                    db.execute("UPDATE leave SET Choice = ? WHERE GuildID = ?", choice, message.guild.id)
                    db.commit()
                    await message.channel.send(f"⚒  Set leave message to `{choice}`.")

                if guild_id_exists is True and choice == "true":
                    db.execute("UPDATE leave SET Choice = ? WHERE GuildID = ?", choice, message.guild.id)
                    db.commit()
                    await message.channel.send(f"⚒  Set leave message to `{choice}`.")
            except BadArgument:
                await message.channel.send(" Oops! `channel_id` must be an integer type value!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        option = db.field("SELECT Choice FROM leave WHERE GuildID = ?", member.guild.id)
        channel_id = db.field("SELECT ChannelID FROM leave WHERE GuildID = ?", member.guild.id)
        member_count = len(member.guild.members)
        guild_name = member.guild.name
        guild_name = guild_name.replace(' ', '%20')
        if channel_id == 0:
            pass
        else:
            if option == "true":
                url = f"https://some-random-api.ml/welcome/img/1/stars?type=leave&username={member.name}&discriminator={member.discriminator}&guildName={guild_name}&memberCount={member_count}&avatar={member.avatar_url_as(format='png')}&textcolor=white&font=3&key=KdRrQKvpk35OfxNGIm997pEvC"
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as af:
                        if 300 > af.status >= 200:
                            fp = io.BytesIO(await af.read())
                            file = discord.File(fp, "leave.png")
                            await self.client.get_channel(channel_id).send(file=file, mention_author=False)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        gid = db.cursor.execute("SELECT 1 FROM leave WHERE GuildID = ?", (guild.id,))

        gid_exists = gid.fetchone() is not None
        if gid_exists is not False:
            print(type(guild.id))
            db.execute("DELETE FROM leave WHERE GuildID = ?", guild.id)
            db.commit()


def setup(client):
    client.add_cog(LeaveMsg(client))
