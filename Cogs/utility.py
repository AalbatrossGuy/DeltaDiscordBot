# Coding=UTF8
# !python
# !/usr/bin/env python3

import discord
from discord.ext import commands
from discord.utils import escape_mentions
from lib.db import db
from PIL import Image
from io import BytesIO
from pyzbar.pyzbar import decode
import requests, random, array, qrcode 
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType
import asyncio
from aiohttp import ClientSession
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
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")
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
    @commands.command(name="link", aliases=["invite"])
    async def send_bot_invite_link(self, ctx):
        #embed = discord.Embed(title="Invite Me 🥰", timestamp=ctx.message.created_at, color=discord.Colour.dark_gold(),
        #                      description="Hey there! click on [this link](https://discord.com/api/oauth2/authorize?client_id=830047831972118588&permissions=1610984518&scope=bot) to invite me to your server!")
        #embed.set_thumbnail(
         #   url="https://static.wixstatic.com/media/6e38f1_72944a54fe214e029653f12798bb8136~mv2.png/v1/fill/w_560,h_210,al_c,q_85,usm_0.66_1.00_0.01/6e38f1_72944a54fe214e029653f12798bb8136~mv2.webp")

        #await ctx.channel.send(embed=embed)

        await ctx.send(
                "🥰 Support Me By Inviting Me To Your Server",
                components=[
                    Button(style=ButtonStyle.URL, label="Invite Me!", url="https://discord.com/api/oauth2/authorize?client_id=830047831972118588&permissions=1610984518&scope=bot")
                    ]
                )
    
    @commands.Cog.listener()
    async def on_button_click(self, response):
        await response.respond(
                type=InteractionType.ChannelMessageWithSource, content="Thanks For Inviting Me :)"
                )

    # Utility Command
    @commands.command(name="minfo")
    async def movie_info(self, ctx, *, query: str = None):
        query = query.replace(" ", "%20")
        url = f"https://www.omdbapi.com/?t={query}&apikey=706a1bfd"
        # print(url)
        try:
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
        except KeyError:
            await ctx.channel.send("<:nope:735473789714038874>Oops! No Movie Found :P")

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

    @commands.command(name="paswdgen")
    async def password_generator(self, ctx, len:int):
        if len > 60:
            await ctx.channel.send("Length Cannot Be More Than `50` Characters.")
        else:
            MAX_LEN = len
            
        
            DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
            LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                                'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                                'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                                'z']
            
            UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                                'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                                'Z']
            
            SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                    '*', '(', ')', '<']
            

            COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
            

            rand_digit = random.choice(DIGITS)
            rand_upper = random.choice(UPCASE_CHARACTERS)
            rand_lower = random.choice(LOCASE_CHARACTERS)
            rand_symbol = random.choice(SYMBOLS)
            

            temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
            
            

            for x in range(MAX_LEN - 4):
                temp_pass = temp_pass + random.choice(COMBINED_LIST)
            

                temp_pass_list = array.array('u', temp_pass)
                random.shuffle(temp_pass_list)
            

            password = ""
            for x in temp_pass_list:
                    password = password + x
                    
            
            await ctx.channel.send(f"🔑 Here's Your Password\n```yaml\n{password}```")

    @commands.command(name='wcheck')
    async def weather_details(self, ctx, *, query:str):
        url = f"http://api.openweathermap.org/data/2.5/weather?appid=77f5585dd715ec1e39ba87b818b44498&q={query}"

        response = requests.request("GET", url=url)
        # For debugging purpose
        # print(response)
        data = response.json()
        # print(data)
        longitude = data['coord']['lon']
        latitude = data['coord']['lat']
        # print(longitude, latitude)
        cloud_type = data['weather'][0]['description']
        # print(cloud_type)
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        temp = (temp - 273.15).__format__('0.2f')
        feels_like = (feels_like - 273.15).__format__('0.2f')
        # print(temp, feels_like)
        min_temp = data['main']['temp_min']
        min_temp = (min_temp - 273.15).__format__('0.2f')
        max_temp = data['main']['temp_max']
        max_temp = (max_temp - 273.15).__format__('0.2f')
        pressure = data['main']['pressure'] # unit hPa
        humidity = data['main']['humidity'] # unit percentage
        wind_speed = data['wind']['speed']
        # print(min_temp, max_temp, pressure, humidity, wind_speed)
        country = data['sys']['country']
        city_name = data['name']

        embed=discord.Embed(title=f"⛅ {city_name}'s Weather Info", timestamp=ctx.message.created_at, color=ctx.message.author.colour)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://i.pinimg.com/originals/e7/7a/60/e77a6068aa8bb2731e3b6d835c09c84c.gif")

        # content
        embed.add_field(name="City", value=city_name)
        embed.add_field(name="Country", value=country)
        embed.add_field(name="Longitude", value=longitude)
        embed.add_field(name="Latitude", value=latitude)
        embed.add_field(name="Cloud Type", value=cloud_type)
        embed.add_field(name="Temperature", value=f"{temp}℃")
        embed.add_field(name="Feels Like", value=f"{feels_like}℃")
        embed.add_field(name="Minimum Temperature", value=f"{min_temp}℃")
        embed.add_field(name="Maximum Temperature", value=f"{max_temp}℃")
        embed.add_field(name="Pressure", value=f"{pressure}hPa")
        embed.add_field(name="Wind Speed", value=f"{wind_speed}m/s")
        embed.add_field(name="Humidity", value=f"{humidity}%")
        await ctx.channel.send(embed=embed)
    
    @commands.command(name='qr')
    async def qr_code_gen(self, ctx, size, *, encode:str) -> BytesIO:
        qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=size, 
                border=4,
                )
        qr.add_data(f'{encode}')
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        buffer_obj = BytesIO()
        img.save(buffer_obj, 'png')

        with BytesIO() as imgbytes:
            img.save(imgbytes, 'png')
            imgbytes.seek(0)
            read_image = buffer_obj.read()
            await ctx.channel.send(
                    file=discord.File(fp=imgbytes, filename='qrcode.png')
                    )
        #img.show()

    @commands.command(name='qrdec')
    async def qr_code_decode(self, ctx):
        image = ctx.message.attachments[0].url

        image = Image.open(requests.get(url=image, stream=True).raw)
        
        result = decode(image)
        for decoded in result:
            await ctx.channel.send(f"🕵️ Decoded Data Is:\n```{decoded.data.decode('utf-8')}```")

    @commands.command(name='cheatsh')
    async def cheat_sh_data(self, ctx, language:str, *, query):
        query = query.replace(" ", "%20")
        url = f"https://cheat.sh/{language}/{query}"
        response = requests.request("GET", url=url)
        await ctx.channel.send(f"```{language}\n{response.text[:1900]}```")

    @commands.command(name='socials')
    async def social_links(self, ctx):
        embed=discord.Embed(title="<:drake_yes:773487910673580043> Socials", color=discord.Color.dark_gold(), timestamp=ctx.message.created_at)
        embed.add_field(name="<:github:851778689648689152> Github", value="[github](https://github.com/AaalbatrossGuy)")
        embed.add_field(name="<:yt:851778739347783740> YouTube #1", value="[youtube](https://www.youtube.com/channel/UC6WW1pBnNICD4Xz4abrU4rg)")
        embed.add_field(name="<:yt:851778739347783740> YouTube #2", value="[youtube](https://www.youtube.com/channel/UC6cFR07R5toAZKZ3hToKgyw)")
        embed.add_field(name="<:instagram:851778716429189140> Instagram", value="[instagram](https://www.instagram.com/xcelsiorplayz/)")
        embed.set_thumbnail(url="https://assets.website-files.com/5e4ef646507f139934406108/5e52e73aeba259d1553eee29_blog-post-5.jpeg")
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)

        await ctx.send(
              embed=embed
                )
    
    @commands.command(name='shell')
    @commands.is_owner()
    async def run_shell_cmds(self, ctx,*, cmd:str):
        process = await asyncio.create_subprocess_shell(
                cmd, stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
                )
        stdout, stderr = await process.communicate()
        
        if stdout:
            await ctx.channel.send(f"```[stdout]\n{stdout.decode()[:1800]}```")
        if stderr:
            await ctx.channel.send(f"```[stderr]\n{stderr.decode()[:1800]}```")


def setup(client):
    DiscordComponents(client)
    client.add_cog(Utilities(client))
