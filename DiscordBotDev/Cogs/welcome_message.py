# Coding=UTF8
# !python
# !/usr/bin/env python3

import discord, requests
from discord.ext import commands
from DiscordBotDev.lib.db import db
from discord.ext.commands.errors import BadArgument
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from io import BytesIO


def mask_circle_transparent(pil_img, blur_radius, offset=0):
    offset = blur_radius * 2 + offset
    mask = Image.new("L", pil_img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((offset, offset, pil_img.size[0] - offset, pil_img.size[1] - offset), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))

    result = pil_img.copy()
    result.putalpha(mask)

    return result


def _add_corners(im, rad=100):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, "white")
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im


class WelcomeMsg(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(manage_guild=True)
    @commands.command(name="set_welcomemsg")
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
    @commands.command(name="update_welcomemsg")
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
        if channel_id == 0:
            pass
        else:
            if option == "true":
                # await self.client.get_channel(channel_id).send("This is a test msg")
                avatar_url = member.avatar_url
                img1 = Image.open(r"Pictures/WelcomeImage.jpg")
                img1 = _add_corners(img1)
                draw = ImageDraw.Draw(img1)
                # print(img1.size)
                font = ImageFont.truetype(r"Fonts/ZenDots-Regular.ttf", 30)

                draw.text((300, 100), f"Welcome to {member.guild.name}", (0, 0, 0), font=font)
                draw.text((350, 500), f"You are member no. #{member_count}", (0, 0, 0), font=font)
                # Opening the secondary image (overlay image)
                img2 = Image.open(requests.get(url=avatar_url, stream=True).raw).convert("RGB")

                img2 = mask_circle_transparent(img2, blur_radius=3)

                # buf = BytesIO()
                #
                # img1.save(buf, 'jpeg')

                # Pasting img2 image on top of img1
                # starting at coordinates (0, 0)
                img1.paste(img2, (420, 140), mask=img2)
                with BytesIO() as image_bytes:
                    img1.save(image_bytes, 'png')
                    image_bytes.seek(0)

                    # buf.seek(0)

                    # img_bytes = buf.read()

                    await self.client.get_channel(channel_id).send(
                        file=discord.File(fp=image_bytes, filename="image.png"))

                # Displaying the image
                # img1.show()
            else:
                pass


def setup(client):
    client.add_cog(WelcomeMsg(client))
