# Coding=UTF8
# !python
# !/usr/bin/env python3


import discord
import requests
from discord.ext import commands
from io import BytesIO
from PIL import Image, ImageOps, ImageFilter
from asyncdagpi import Client, ImageFeatures

class ImageManipulation(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.dagpi = Client("MTYyMzUwMzMzMQ.876re9HvmxvFcf41LIotTu2WrHC5VNPc.edc4473be1c68f30")

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

    @commands.command()
    async def wasted(self, ctx, *, member:discord.Member = None):
        member = member or ctx.message.author
        url = member.avatar_url_as(format="png")
        base_url = f"https://some-random-api.ml/canvas/wasted?avatar={url}"
        await ctx.channel.send(base_url)

    @commands.command()
    async def trigger(self, ctx, *, member:discord.Member = None):
        member = member or ctx.message.author
        url= member.avatar_url_as(format="png")
        img = await self.dagpi.image_process(ImageFeatures.triggered(), str(url))
        file = discord.File(fp=img.image, filename=f"triggered.{img.format}")
        await ctx.channel.send(file=file)

    @commands.command()
    async def magic(self, ctx, *, member:discord.Member = None):
        member = member or ctx.message.author
        url = member.avatar_url_as(format="png")
        img  = await self.dagpi.image_process(ImageFeatures.magik(), str(url))
        file = discord.File(fp=img.image, filename=f"magic.{img.format}")
        await ctx.channel.send(file=file)

    @commands.command()
    async def pixel(self, ctx, *, member:discord.Member = None):
        member = member or ctx.message.author
        url = member.avatar_url_as(format="png")
        img = await self.dagpi.image_process(ImageFeatures.pixel(), str(url))
        file = discord.File(fp=img.image, filename=f'pixel.{img.format}')
        await ctx.channel.send(file=file)

    @commands.command()
    async def angel(self, ctx, *, member:discord.Member = None):
        member = member or ctx.message.author
        url = member.avatar_url_as(format="png")
        img = await self.dagpi.image_process(ImageFeatures.angel(), str(url))
        file = discord.File(fp=img.image, filename=f"angel.{img.format}")
        await ctx.channel.send(file=file)

    @commands.command()
    async def devil(self, ctx, *, member:discord.Member = None):
        member = member or ctx.message.author
        url = member.avatar_url_as(format="png")
        img = await self.dagpi.image_process(ImageFeatures.satan(), str(url))
        file = discord.File(fp=img.image, filename=f"devil.{img.format}")
        await ctx.channel.send(file=file)


    @commands.command()
    async def windel(self, ctx, *, member:discord.Member = None):
        member = member or ctx.message.author
        url = member.avatar_url_as(format="png")
        img = await self.dagpi.image_process(ImageFeatures.delete(), str(url))
        file = discord.File(fp=img.image, filename=f'delete.{img.format}')
        await ctx.channel.send(file=file)

    @commands.command()
    async def hitler(self, ctx, *, member:discord.Member = None):
        member = member or ctx.message.author
        url = member.avatar_url_as(format="png")
        img = await self.dagpi.image_process(ImageFeatures.hitler(), str(url))
        file = discord.File(fp=img.image, filename=f'hitler.{img.format}')
        await ctx.channel.send(file=file)

    @commands.command()
    async def stringify(self, ctx, *, member:discord.Member = None):
        member = member or ctx.message.author
        url = member.avatar_url_as(format="png")
        img = await self.dagpi.image_process(ImageFeatures.stringify(), str(url))
        file = discord.File(fp=img.image, filename = f"stringify.{img.format}")
        await ctx.channel.send(file=file)



def setup(client):
    client.add_cog(ImageManipulation(client))
