# Coding=UTF8
# !python
# !/usr/bin/env python3

import discord, aiohttp, io
from discord.ext import commands
from lib import db
from discord.ext.commands.errors import BadArgument


# def mask_circle_transparent(pil_img, blur_radius, offset=0):
#     offset = blur_radius * 2 + offset
#     mask = Image.new("L", pil_img.size, 0)
#     draw = ImageDraw.Draw(mask)
#     draw.ellipse((offset, offset, pil_img.size[0] - offset, pil_img.size[1] - offset), fill=255)
#     mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))

#     result = pil_img.copy()
#     result.putalpha(mask)

#     return result


# def _add_corners(im, rad=100):
#     circle = Image.new('L', (rad * 2, rad * 2), 0)
#     draw = ImageDraw.Draw(circle)
#     draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
#     alpha = Image.new('L', im.size, "white")
#     w, h = im.size
#     alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
#     alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
#     alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
#     alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
#     im.putalpha(alpha)
#     return im


class WelcomeMsg(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(manage_guild=True)
    @commands.command(name="set_welcome")
    async def set_welcome_message(self, message, channel_id: int = 0, choice: str = "false"):

        # Checks if the guild id exists in database or not

        guild_id = db.cursor.execute("SELECT 1 FROM welcome WHERE GuildID = ? ",
                                     (message.guild.id,))

        guild_id_exists = guild_id.fetchone() is not None

        # Does a simple check to see if the guild id exists or not...if it doesn't, then raise error else insert data

        if guild_id_exists is False and channel_id == 0:
            await message.channel.send("⚒  Oops! You cannot switch welcome message off unless u switch it on!")
        elif guild_id_exists is False and channel_id != 0:
            db.execute("INSERT OR IGNORE INTO welcome(GuildID, ChannelID, Choice) VALUES(?,?,?)",
                       (message.guild.id),
                       (channel_id), (choice))
            db.commit()
            await message.channel.send("⚒  Switched on welcome message!")

            # await message.channel.send(" Oops! `channel_id` must be an integer type value!")

    @commands.has_permissions(manage_guild=True)
    @commands.command(name="update_welcome")
    async def update_welcome_message(self, message, choice: str = "false"):
        guild_id = db.cursor.execute("SELECT 1 FROM welcome WHERE GuildID = ? ",
                                     (message.guild.id,))

        guild_id_exists = guild_id.fetchone() is not None

        if guild_id_exists is False:
            await message.channel.send("⚒  Oops! You have to set welcome message first before using this command.")
        else:
            # Updates the database

            try:
                if guild_id_exists is True and choice == "false":
                    db.execute("UPDATE welcome SET Choice = ? WHERE GuildID = ?", choice, message.guild.id)
                    db.commit()
                    await message.channel.send(f"⚒  Set welcome message to `{choice}`.")

                if guild_id_exists is True and choice == "true":
                    db.execute("UPDATE welcome SET Choice = ? WHERE GuildID = ?", choice, message.guild.id)
                    db.commit()
                    await message.channel.send(f"⚒  Set welcome message to `{choice}`.")
            except BadArgument:
                await message.channel.send(" Oops! `channel_id` must be an integer type value!")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        db.execute("DELETE FROM welcome WHERE GuildID = ?", guild.id)
        db.commit()

    @commands.Cog.listener()
    async def on_member_join(self, member):

        option = db.field("SELECT Choice FROM welcome WHERE GuildID = ?", member.guild.id)
        channel_id = db.field("SELECT ChannelID FROM welcome WHERE GuildID = ?", member.guild.id)
        member_count = len(member.guild.members)
        guild_name = member.guild.name
        guild_name = guild_name.replace(' ', '%20')
        if channel_id == 0:
            pass
        else:
            if option == "true":
                url = f"https://some-random-api.ml/welcome/img/1/sunset?type=join&username={member.name}&discriminator={member.discriminator}&guildName={guild_name}&memberCount={member_count}&avatar={member.avatar_url_as(format='png')}&font=3&textcolor=black&key=KdRrQKvpk35OfxNGIm997pEvC"
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as af:
                        if 300 > af.status >= 200:
                            fp = io.BytesIO(await af.read())
                            file = discord.File(fp, "welcome.png")
                            await self.client.get_channel(channel_id).send(file=file, mention_author=False)
            # await self.client.get_channel(channel_id).send(f'{member.name}, {member.discriminator}, {guild_name}, {member.avatar_url_as(format="png")}')
            else:
                pass


def setup(client):
    client.add_cog(WelcomeMsg(client))
