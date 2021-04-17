# Coding=UTF8
# !python
# !/usr/bin/env python3


import discord
import requests
from discord.ext import commands
from io import BytesIO
from PIL import Image, ImageOps, ImageFilter


class ImageManipulation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="bw_u")
    async def black_and_white_user(self, ctx, *, member: discord.Member = None):
        member = member or ctx.message.author
        avatar_url = member.avatar_url_as(format='jpeg')
        image = Image.open(requests.get(url=avatar_url, stream=True).raw).convert("L")

        with BytesIO() as image_bytes:
            image.save(image_bytes, 'jpeg')
            image_bytes.seek(0)

            await ctx.channel.send(
                file=discord.File(fp=image_bytes, filename="image.jpeg"))

    @commands.command(name="negative_u")
    async def negative_user(self, ctx, *, member: discord.Member = None):
        member = member or ctx.message.author
        avatar_url = member.avatar_url_as(format='jpeg')
        image = Image.open(requests.get(url=avatar_url, stream=True).raw)
        image_inverted = ImageOps.invert(image)

        with BytesIO() as image_bytes:
            image_inverted.save(image_bytes, 'jpeg')
            image_bytes.seek(0)
            await ctx.channel.send(
                file=discord.File(fp=image_bytes, filename="image.jpeg"))

    @commands.command(name="blur_u")
    async def blur_user(self, ctx, radius: int, *, member: discord.Member = None):
        member = member or ctx.message.author
        avatar_url = member.avatar_url_as(format='jpeg')
        image = Image.open(requests.get(url=avatar_url, stream=True).raw)
        blurred_image = image.filter(ImageFilter.GaussianBlur(radius=int(radius)))

        with BytesIO() as image_bytes:
            blurred_image.save(image_bytes, 'jpeg')
            image_bytes.seek(0)
            await ctx.channel.send(
                file=discord.File(fp=image_bytes, filename="image.jpeg"))

    @commands.command(name="bw_f")
    async def black_and_white_file(self, ctx):
        image = ctx.message.attachments[0].url
        main_image = Image.open(requests.get(url=image, stream=True).raw).convert("L")

        with BytesIO() as image_bytes:
            main_image.save(image_bytes, 'jpeg')
            image_bytes.seek(0)

            await ctx.channel.send(
                file=discord.File(fp=image_bytes, filename="image.jpeg"))

    @commands.command(name="negative_f")
    async def negative_file(self, ctx):
        image = ctx.message.attachments[0].url
        image = Image.open(requests.get(url=image, stream=True).raw).convert("RGB")
        main_image = ImageOps.invert(image)

        with BytesIO() as image_bytes:
            main_image.save(image_bytes, 'jpeg')
            image_bytes.seek(0)

            await ctx.channel.send(
                file=discord.File(fp=image_bytes, filename="image.jpeg"))

    @commands.command(name="blur_f")
    async def blur_file(self, ctx, radius: int):
        image = ctx.message.attachments[0].url

        image = Image.open(requests.get(url=image, stream=True).raw)
        main_image = image.filter(ImageFilter.GaussianBlur(radius=int(radius)))

        with BytesIO() as image_bytes:
            main_image.save(image_bytes, 'png')
            image_bytes.seek(0)
            await ctx.channel.send(
                file=discord.File(fp=image_bytes, filename="image.png"))


def setup(client):
    client.add_cog(ImageManipulation(client))
