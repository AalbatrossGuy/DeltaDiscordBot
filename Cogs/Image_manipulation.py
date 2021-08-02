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


    #Error Handlers

    @black_and_white_user.error
    async def bw_user_error_handling(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Member Not Found", description="```ini\nMake sure you have run the command providing the [username]```", timestamp=ctx.message.created_at, color=discord.Color.dark_red()))


    @negative_user.error
    async def negative_u_error_handling(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Member Not Found", description="```ini\nMake sure you have run the command providing the [username]```", timestamp=ctx.message.created_at, color=discord.Color.dark_red()))


    @blur_user.error 
    async def blur_u_error_handling(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Member Not Found", description="```ini\nMake sure you have run the command providing the [username]```", timestamp=ctx.message.created_at, color=discord.Color.dark_red()))

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Arguments", description="```ini\nMake sure you have run the command providing the [blur radius] and the [username]```", timestamp=ctx.message.created_at, color=discord.Color.dark_teal()))


    @black_and_white_file.error 
    async def bw_f_error_handling(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Attachment", description="```prolog\nMake sure you have run the command providing the File/Image as an Attachment```", timestamp=ctx.message.created_at, color=discord.Color.dark_teal()))

    @negative_file.error 
    async def negative_f_error_handling(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Attachment", description="```prolog\nMake sure you have run the command providing the File/Image as an Attachment```", timestamp=ctx.message.created_at, color=discord.Color.dark_teal()))

    @blur_file.error 
    async def blur_f_error_handling(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Attachment", description="```prolog\nMake sure you have run the command providing the File/Image as an Attachment```", timestamp=ctx.message.created_at, color=discord.Color.dark_teal()))


    @wasted.error
    async def wasted_error_handling(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Member Not Found", description="```ini\nMake sure you have run the command providing the [username]```", timestamp=ctx.message.created_at, color=discord.Color.dark_red()))

    @trigger.error
    async def trigger_error_handling(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Member Not Found", description="```ini\nMake sure you have run the command providing the [username]```", timestamp=ctx.message.created_at, color=discord.Color.dark_red()))

    @magic.error
    async def magic_error_handling(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Member Not Found", description="```ini\nMake sure you have run the command providing the [username]```", timestamp=ctx.message.created_at, color=discord.Color.dark_red()))


    @pixel.error
    async def pixel_error_handling(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Member Not Found", description="```ini\nMake sure you have run the command providing the [username]```", timestamp=ctx.message.created_at, color=discord.Color.dark_red()))


    @angel.error
    async def angel_error_handling(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Member Not Found", description="```ini\nMake sure you have run the command providing the [username]```", timestamp=ctx.message.created_at, color=discord.Color.dark_red()))

    @devil.error
    async def devil_error_handling(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Member Not Found", description="```ini\nMake sure you have run the command providing the [username]```", timestamp=ctx.message.created_at, color=discord.Color.dark_red()))

    @windel.error
    async def windel_error_handling(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Member Not Found", description="```ini\nMake sure you have run the command providing the [username]```", timestamp=ctx.message.created_at, color=discord.Color.dark_red()))


    @hitler.error
    async def hitler_error_handling(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Member Not Found", description="```ini\nMake sure you have run the command providing the [username]```", timestamp=ctx.message.created_at, color=discord.Color.dark_red()))


    @stringify.error
    async def stringify_error_handling(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Member Not Found", description="```ini\nMake sure you have run the command providing the [username]```", timestamp=ctx.message.created_at, color=discord.Color.dark_red()))




def setup(client):
    client.add_cog(ImageManipulation(client))
