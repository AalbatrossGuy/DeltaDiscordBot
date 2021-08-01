# Coding=UTF8
# !python3
# /usr/bin/env python3

import discord, random, requests
from discord.ext import commands
import aiohttp, io, asyncio
from discord_components import DiscordComponents, Select, SelectOption
from datetime import timedelta



class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="predict")
    async def predict(self, ctx, *, question:str):
        responses = [
            "yes", "ok", "i don't know", "no", "absolutely not"
        ]

        await ctx.channel.send(f"{random.random(responses)}")

    @commands.command(name='ytcomm')
    async def youtube_comment_fake(self, ctx, username: discord.Member, *, comment):
        avatar = username.avatar_url_as(format='png')
        # str(username).split('#')[0] strip the discriminator
        comment = comment.replace(" ", "+")
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/youtube-comment?username={str(username).split("#")[0]}&comment={comment}&avatar={avatar}'
            ) as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "ytcomment.png")
                    em = discord.Embed(
                        title="Nice Comment ;)",
                        color=discord.Color.dark_red(),
                    )
                    em.set_image(url="attachment://ytcomment.png")
                    await ctx.reply(embed=em, file=file, mention_author=False)
                    
                else:
                    await ctx.reply('Oops! An error occured. Please Try Again Later.')
                await session.close()

    @commands.command(name="twt")
    async def tweet_fake(self, ctx, username: discord.Member, *, comment):
        avatar = username.avatar_url_as(format='png')
        comment = comment.replace(" ", "+")
        if username.nick == None : nick_name = str(username).split("#")[0]
        else: nick_name = username.nick
        #url = "https://some-random-api.ml/canvas/tweet?avatar=https://cdn.discordapp.com/avatars/560789882738573324/bc220b0eeeabbe234026e4881f3c3b9c.png&username=Telk&displayname=TAl&comment=Hello"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/tweet?avatar={avatar}&username={str(username).split("#")[0]}&displayname={nick_name}&comment={comment}'
            ) as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "tweet.png")
                    em = discord.Embed(
                        title="Nice Tweet ;)",
                        color=discord.Color.dark_red(),
                    )
                    em.set_image(url="attachment://tweet.png")
                    await ctx.reply(embed=em, file=file, mention_author=False)
                    
                else:
                    await ctx.reply('Oops! An error occured. Please Try Again Later.')
                await session.close()
    
    @commands.command(name="pet")
    async def petpat(self, ctx, username: discord.Member = None):
        username = username or ctx.author
        avatar = username.avatar_url_as(format='png')
        url = f"https://some-random-api.ml/premium/petpet?avatar={avatar}&key=KdRrQKvpk35OfxNGIm997pEvC"
        #print(url)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "petpat.gif")
                    await ctx.reply(file=file, mention_author=False)
                    
                else:
                    await ctx.reply('Oops! An error occured. Please Try Again Later.')
                    await session.close()

    @commands.command(name="fact")
    async def animal_facts(self, ctx):
        embed=discord.Embed(title="<a:panda:871255104735567912> Animal Facts", timestamp=ctx.message.created_at, color=discord.Color.dark_orange(), description="Click on the drop down menu and select what fact do you want to know.")
        embed.set_thumbnail(url='https://media.wired.com/photos/593261cab8eb31692072f129/master/pass/85120553.jpg')
        embed.set_author(name="Love animals", icon_url='https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg')

        urlPanda = "https://some-random-api.ml/animal/panda"
        responsePanda = requests.request("GET", url=urlPanda)
        dataPanda = responsePanda.json()
        imagePanda = dataPanda['image']
        factPanda = dataPanda['fact']

        embedPanda = discord.Embed(title="A Panda Fact", timestamp=ctx.message.created_at, color=discord.Color.dark_theme(), description=factPanda)
        embedPanda.set_footer(text='Delta Δ is the fourth letter of the Greek Alphabet', icon_url=ctx.author.avatar_url)
        embedPanda.set_image(url=imagePanda)

        urlDog = "https://some-random-api.ml/animal/dog"
        responseDog = requests.request("GET", url=urlDog)
        imageDog = responseDog.json()['image']
        factDog = responseDog.json()['fact']

        embedDog = discord.Embed(title="A Dog Fact", timestamp=ctx.message.created_at, color=discord.Color.dark_grey(), description=factDog)
        embedDog.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embedDog.set_image(url=imageDog)

        urlFox = "https://some-random-api.ml/animal/fox"
        responseFox = requests.request("GET", url=urlFox)
        imageFox = responseFox.json()['image']
        factFox = responseFox.json()['fact']

        embedFox = discord.Embed(title="A Fox Fact", timestamp=ctx.message.created_at, color=discord.Color.dark_blue(), description=factFox)
        embedFox.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embedFox.set_image(url=imageFox)

        urlKoala = "https://some-random-api.ml/animal/koala"
        responseKoala = requests.request("GET", url=urlKoala)
        imageKoala = responseKoala.json()['image']
        factKoala = responseKoala.json()['fact']

        embedKoala = discord.Embed(title="A Koala Fact", timestamp=ctx.message.created_at, color=discord.Color.dark_gold(), description=factKoala)
        embedKoala.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embedKoala.set_image(url=imageKoala)

        urlBird = "https://some-random-api.ml/animal/birb"
        responseBird = requests.request("GET", url=urlBird)
        imageBird = responseBird.json()['image']
        factBird = responseBird.json()['fact']

        embedBird = discord.Embed(title="A Bird Fact", timestamp=ctx.message.created_at, color=discord.Color.dark_purple(), description=factBird)
        embedBird.set_footer(text='Delta Δ is the fourth letter of the Greek Alphabet', icon_url=ctx.author.avatar_url)
        embedBird.set_image(url=imageBird)

        tdelta = ctx.message.created_at + timedelta(minutes=1)

        await ctx.reply(embed=embed, components=[
            Select(
                placeholder="Select a Fact Category",
                min_values=1,
                options=[
                SelectOption(label="🐼 Panda", value="Select this to get a randomly generated Panda fact"),
                SelectOption(label="🐶 Dog", value="Select this to get a randomly generated Dog fact"),
                SelectOption(label="🦊 Fox", value="Select this to get a randomly generated Fox fact"),
                SelectOption(label="🐨 Koala", value="Select this to get a randomly generated Koala fact"),
                SelectOption(label="🐦 Bird", value="Select this to get a randomly generated Bird fact")
                ],
            ),
        ])

        interaction = await self.client.wait_for("select_option", timeout=60)
        if interaction.author.id == ctx.author.id and interaction.message.embeds[0].timestamp < tdelta:
            check_for = interaction.component[0].label
            if check_for.lower() == '🐼 panda':
                await interaction.respond(embed=embedPanda, ephemeral=False)
            elif check_for.lower() == '🐶 dog':
                await interaction.respond(embed=embedDog, ephemeral=False)
            elif check_for.lower() == '🦊 fox':
                await interaction.respond(embed=embedFox, ephemeral=False) 
            elif check_for.lower() == '🐨 koala':
                await interaction.respond(embed=embedKoala, ephemeral=False)
            elif check_for.lower() == '🐦 bird':
                await interaction.respond(embed=embedBird, ephemeral=False)


def setup(client):
    DiscordComponents(client)
    client.add_cog(Fun(client))
