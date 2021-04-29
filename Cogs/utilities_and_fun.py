# Coding=UTF8
# !python
# !/usr/bin/env python3

import discord
from discord.ext import commands
from discord.utils import escape_mentions
from lib.db import db
from aiohttp import ClientSession
import requests


def convert_bytes(bytes_number):
    tags = ["B", "KiB", "MiB", "GB", "TB"]

    i = 0
    double_bytes = bytes_number

    while i < len(tags) and bytes_number >= 1024:
        double_bytes = bytes_number / 1024.0
        i = i + 1
        bytes_number = bytes_number / 1024

    return str(round(double_bytes, 2)) + " " + tags[i]


class Utilities(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Utility Command
    @commands.command(name="avatar")
    async def user_profileimage(self, ctx, *, member: discord.Member = None):
        member = member or ctx.message.author
        jpg = member.avatar_url_as(format='jpg')
        webp = member.avatar_url_as(format='webp')
        png = member.avatar_url_as(format='png')

        embed = discord.Embed(title=f"Avatar of {member}", description=f"[jpg]({jpg}) | [png]({png}) | [webp]({webp})",
                              color=discord.Colour.dark_gold(), timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        # embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")
        embed.set_image(url=member.avatar_url)
        await ctx.channel.send(embed=embed)

    @commands.command(name="set_webhook")
    async def set_bot_webhook(self, ctx):
        guild_id = db.cursor.execute("SELECT 1 FROM webhook WHERE GuildID = ? ",
                                     (ctx.message.guild.id,))
        guild_id_exists = guild_id.fetchone() is not None
        if guild_id_exists is False:
            created_webhook = await ctx.channel.create_webhook(name="SayCmd Webhook")
            url = created_webhook.url
            db.execute("INSERT OR IGNORE INTO webhook(GuildID, Url) VALUES(?, ?)", int(ctx.message.guild.id), str(url))
            db.commit()
            await ctx.channel.send('⚒  Webhook has been created for this channel')
        elif guild_id_exists is True:
            await ctx.channel.send(
                "You have already set the webhook for this channel. For resetting, delete the exisiting webhook by using `delete_webhook` and then type this command.")

    @commands.command(name="delete_webhook")
    async def delete_bot_webhook(self, ctx):
        guild_id = db.cursor.execute("SELECT 1 FROM webhook WHERE GuildID = ? ",
                                     (ctx.message.guild.id,))
        guild_id_exists = guild_id.fetchone() is not None
        if guild_id_exists is False:
            await ctx.channel.send(
                'You cannot delete a webhook unless u have created it. Run `set_webhook` to create a webhook first')
        elif guild_id_exists is True:
            db.execute("DELETE FROM webhook WHERE GuildID = ?", (ctx.message.guild.id))
            db.commit()
            await ctx.channel.send("⚒  The webhook for this channel has been deleted from the database.")

    # Fun Command
    @commands.command(name="say")
    async def say_webhook_command(self, message, *, query: str = 'hello!'):

        async with ClientSession() as session:
            guild_id = db.cursor.execute("SELECT 1 FROM webhook WHERE GuildID = ? ",
                                         (message.guild.id,))
            guild_id_exists = guild_id.fetchone() is not None
            if not guild_id_exists:
                await message.channel.send(
                    "Oops! Tell a mod in the server to run the `set_webhook` command before using this command :)")
            else:
                query = escape_mentions(query)
                webhook_url = db.field("SELECT Url FROM webhook WHERE GuildID = ?", (message.guild.id))

                # print(message.guild.id) Used it for debugging.
                # print(webhook_url) Used it for debugging.
            webhook = discord.Webhook.from_url(webhook_url, adapter=discord.AsyncWebhookAdapter(session))
            await message.channel.purge(limit=1)
            await webhook.send(content=query, username=message.author.name, avatar_url=message.author.avatar_url)

    # Utility Command
    @commands.command(name="link")
    async def send_bot_invite_link(self, ctx):
        embed = discord.Embed(title="Invite Me 🥰", timestamp=ctx.message.created_at, color=discord.Colour.dark_gold(),
                              description="Hey there! click on [this link](https://discord.com/api/oauth2/authorize?client_id=830047831972118588&permissions=1610984518&scope=bot) to invite me to your server!")
        embed.set_thumbnail(
            url="https://static.wixstatic.com/media/6e38f1_72944a54fe214e029653f12798bb8136~mv2.png/v1/fill/w_560,h_210,al_c,q_85,usm_0.66_1.00_0.01/6e38f1_72944a54fe214e029653f12798bb8136~mv2.webp")

        await ctx.channel.send(embed=embed)

    # Utility Command
    @commands.command(name="minfo")
    async def movie_info(self, ctx, *, query: str = None):
        query = query.replace(" ", "%20")
        url = f"https://www.omdbapi.com/?t={query}&apikey=706a1bfd"
        # print(url)
        response = requests.request("GET", url=url)
        data = response.json()
        # print(data)
        title = data['Title']
        rated = data['Rated']
        released = data['Released']
        length = data['Runtime']
        genre = data['Genre']
        director = data['Director']
        writer = data['Writer']
        actors = data['Actors']
        language = data['Language']
        country = data['Country']
        awards = data['Awards']
        Poster_Img = data['Poster']
        rating = data['imdbRating']
        votes = data['imdbVotes']
        movie_type = data['Type']
        boxoffice = data['BoxOffice']
        plot = data['Plot']
        # ---------------- Embed -----------------

        embed = discord.Embed(title=f"{title}", timestamp=ctx.message.created_at, color=ctx.message.author.colour)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_image(url=Poster_Img)
        embed.add_field(name="Title", value=title, inline=True)
        embed.add_field(name="Director", value=director, inline=True)
        embed.add_field(name="Writer(s)", value=writer, inline=True)
        embed.add_field(name="Actor(s)", value=actors, inline=True)
        embed.add_field(name="Plot", value=plot, inline=True)
        embed.add_field(name="Length", value=length, inline=True)
        embed.add_field(name="Genre", value=genre, inline=True)
        embed.add_field(name="Release Date", value=released, inline=True)
        embed.add_field(name="Rated", value=rated, inline=True)
        embed.add_field(name="Language", value=language, inline=True)
        embed.add_field(name="Country", value=country, inline=True)
        embed.add_field(name="Awards", value=awards, inline=True)
        embed.add_field(name="Imdb Rating", value=rating, inline=True)
        embed.add_field(name="Votes", value=votes, inline=True)
        embed.add_field(name="Boxoffice", value=boxoffice, inline=True)
        embed.add_field(name="Type", value=movie_type, inline=True)

        await ctx.channel.send(embed=embed)

    # Utility command
    @commands.command(name="sinfo")
    async def server_info(self, ctx):

        member_statuses = [
            len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
            len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
            len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
            len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))
        ]
        guild_icon = ctx.guild.icon_url
        guild_name = ctx.guild.name
        guild_id = ctx.guild.id
        guild_owner = ctx.guild.owner
        guild_owner_id = ctx.guild.owner_id
        guild_region = ctx.guild.region
        guild_created_at = ctx.guild.created_at.strftime("%d/%m/%y %H:%M:%S")
        guild_members = len(ctx.guild.members)
        guild_humans = len(list(filter(lambda m: not m.bot, ctx.guild.members)))
        guild_bots = len(list(filter(lambda m: m.bot, ctx.guild.members)))
        guild_member_statuses = f":green_circle: {member_statuses[0]} :yellow_circle: {member_statuses[1]} :red_circle: {member_statuses[2]} :white_circle: {member_statuses[3]}"
        guild_text_channels = len(ctx.guild.text_channels)
        guild_voice_channels = len(ctx.guild.voice_channels)
        guild_categories = len(ctx.guild.categories)
        guild_roles = len(ctx.guild.roles)
        guild_emoji_limit = ctx.guild.emoji_limit
        guild_filesize_limit = ctx.guild.filesize_limit

        # ------------- Embed --------------------

        embed = discord.Embed(title=f"{guild_name}'s Information", timestamp=ctx.message.created_at,
                              colour=ctx.message.author.colour)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=guild_icon)
        embed.add_field(name="🤠 Guild Owner", value=guild_owner, inline=True)
        embed.add_field(name="🤠 Owner ID", value=guild_owner_id, inline=True)
        embed.add_field(name=" <:foxia:832549597892313159> Guild Name", value=guild_name, inline=True)
        embed.add_field(name="<:foxia:832549597892313159> Guild ID", value=guild_id, inline=True)
        embed.add_field(name="🌏 Guild Region", value=guild_region, inline=True)
        embed.add_field(name="🕐 Guild Created At", value=guild_created_at, inline=True)
        embed.add_field(name="🧑‍🤝‍🧑 Guild Humans", value=str(guild_humans))
        embed.add_field(name="<:bot:773145401611255808> Guild Bots", value=str(guild_bots))
        embed.add_field(name="♾️ Guild Members", value=str(guild_members))
        embed.add_field(name="👻 Member Statuses", value=guild_member_statuses)
        embed.add_field(name="📰 Guild Text Channels", value=f"\t{str(guild_text_channels)}")
        embed.add_field(name="🎙️ Guild Voice Channels", value=str(guild_voice_channels))
        embed.add_field(name="<:owo:773057515826708501> Guild Categories", value=str(guild_categories))
        embed.add_field(name="<:sweet:773054385542266880> Guild Roles", value=str(guild_roles))
        embed.add_field(name="🙂 Guild Emoji Limit", value=guild_emoji_limit)
        embed.add_field(name="📂 Guild Max Filelimit", value=f"{convert_bytes(guild_filesize_limit)}")
        await ctx.channel.send(embed=embed)

    @commands.command(name="meminfo")
    async def member_info_command(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        member_id = member.id
        member_name = str(member.name)
        member_avatar_url = member.avatar_url
        member_nickname = str(member.nick)
        is_bot = member.bot
        member_top_role = member.top_role.mention
        member_status = str(member.status).title()
        member_activity = f"{str(member.activity.type).split('.')[-1].title() if member.activity else 'No Activity'} {member.activity.name if member.activity else ''}"
        member_created_at = member.created_at.strftime("%d/%m/%Y %H:%M:%S")
        member_joined_at = member.joined_at.strftime("%d/%m/%Y %H:%M:%S")
        member_has_nitro = str(bool(member.premium_since))

        # ---------------- Embed ---------------------

        embed = discord.Embed(title=f"{member_name}'s Information", timestamp=ctx.message.created_at, color=ctx.message.author.colour)
        embed.add_field(name="<:foxia:832549597892313159> Name", value=member_name, inline=True)
        embed.add_field(name="<:foxia:832549597892313159> ID", value=member_id, inline=True)
        embed.add_field(name="<:foxia:832549597892313159> Nickname", value=member_nickname, inline=True)
        embed.add_field(name="<:bot:773145401611255808> BOT?", value=is_bot, inline=True)
        embed.add_field(name="<:top:836901077638447134> Top Role", value=member_top_role, inline=True)
        embed.add_field(name="<:pandacop:831800704372178944> Activity", value=member_activity, inline=True)
        embed.add_field(name="🕦 Created At", value=member_created_at, inline=True)
        embed.add_field(name=":clock8: Joined At", value=member_joined_at, inline=True)
        embed.add_field(name="<a:nitrobaby:836902390766108694> Nitro?", value=member_has_nitro, inline=True)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=member_avatar_url)
        await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(Utilities(client))
