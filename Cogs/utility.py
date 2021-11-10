# Coding=UTF8
# !python
# !/usr/bin/env python3

import discord
from discord.ext import commands
from discord.utils import escape_mentions
from lib import db
from io import BytesIO
import requests, random, array, asyncio
from aiohttp import ClientSession
from datetime import timezone
from currency_converter import CurrencyConverter
from customs.customs import circle
from PIL import Image, ImageDraw, ImageFont  
import dateutil.parser



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
                "You have already set the webhook for this channel. For resetting, delete the existing webhook by using `delete_webhook` and then type this command.")

    @commands.command(name="delete_webhook")
    async def delete_bot_webhook(self, ctx):
        guild_id = db.cursor.execute("SELECT 1 FROM webhook WHERE GuildID = ? ",
                                     (ctx.message.guild.id,))
        guild_id_exists = guild_id.fetchone() is not None
        if guild_id_exists is False:
            await ctx.channel.send(
                'You cannot delete a webhook unless u have created it. Run `set_webhook` to create a webhook first')
        elif guild_id_exists is True:
            db.execute("DELETE FROM webhook WHERE GuildID = ?ox variable stores th", (ctx.message.guild.id))
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

    @commands.command(name='chlog')
    async def change_log(self,  ctx):
        embed = discord.Embed(title="Change Log", timestamp=ctx.message.created_at, color=ctx.message.author.colour)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="http://converseen.fasterland.net/wp-content/uploads/2014/05/Changelog.png")
        embed.add_field(name="📃 The Change Logs for Delta:", value="```diff\n+ Fixed some small typos and bugs[BUG-FIX]\n+Added Log functionality (Optional) to log all mod commands used in a server[NEW].\n+ Added massban, massunban & masskick commands[NEW].\n- Removed lockdown and unlock commands[DELETE].\n+ Improved UI For help command[IMPROVE].\n+ Added sp command[NEW].\n+ Fixed improper functioning of fact command[BUG-FIX].```")
        await ctx.channel.send(embed=embed)

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
        guild_created_at = int(ctx.guild.created_at.replace(tzinfo=timezone.utc).timestamp())
        guild_members = len(ctx.guild.members)
        guild_humans = len(list(filter(lambda m: not m.bot, ctx.guild.members)))
        guild_bots = len(list(filter(lambda m: m.bot, ctx.guild.members)))
        guild_member_statuses = f"<:online:870496098911940718> {member_statuses[0]} <:idle:870496098999992390> {member_statuses[1]} <:dnd:870496098886746122> {member_statuses[2]} <:offline:870496098874183692> {member_statuses[3]}"
        guild_text_channels = len(ctx.guild.text_channels)
        guild_voice_channels = len(ctx.guild.voice_channels)
        guild_categories = len(ctx.guild.categories)
        guild_roles = len(ctx.guild.roles)
        guild_emoji_limit = ctx.guild.emoji_limit
        guild_filesize_limit = ctx.guild.filesize_limit

        # ------------- Images ------------------


         #print('image gen started')
        name = guild_name
        pfp = ctx.guild.icon_url_as(size=256)
        #print('pfp got')
        data = BytesIO(await pfp.read())
        pfp = Image.open(data).convert("RGBA")
        #print('pfp read')
        base = Image.open("Pictures/base.jpg").convert("RGBA")
        name = f"{name[:16]}..." if len(name) > 16 else name
        #print('base opened name got')
        date = f"Created At: {ctx.guild.created_at.strftime('%d/%m/%Y')}"
        draw = ImageDraw.Draw(base)
        #print('date got got drawing started')
        pfp = circle(pfp)
        font = ImageFont.truetype(r"Fonts/ZenDots-Regular.ttf", 30)
        fontdate = ImageFont.truetype(r"Fonts/ZenDots-Regular.ttf", 20)
        #print('both fonts got')
        draw.text((200, 50), name, font=font, fill="#000000")
        draw.text((200, 100), date, font=fontdate, fill="#000000")
        base.paste(pfp, (30, 30), pfp)
        #print('base pasted...writing done')

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
        embed.add_field(name="🕐 Guild Created At", value=f"<t:{guild_created_at}:F>\n(<t:{guild_created_at}:R>)",
                        inline=True)
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

        with BytesIO() as imgbyte:
            base.save(imgbyte, "PNG")
            imgbyte.seek(0)
            #print('done #1')
            file = discord.File(imgbyte, filename="image.png")
            embed.set_image(url="attachment://image.png")
            #print('done #2')
            await ctx.channel.send(file=file, embed=embed)
            #print('sent')

    
    # Many deubug statements. Please ignore

    @commands.command(name="meminfo")
    async def member_info_command(self, ctx, *, member: discord.Member = None):
        #print('meminfo called')
        member = member or ctx.author
        member_id = member.id
        member_name = str(member.name)
        member_avatar_url = member.avatar_url
        member_nickname = str(member.nick)
        is_bot = member.bot
        member_top_role = member.top_role.mention
        member_status = str(member.status).title()
        member_activity = f"{str(member.activity.type).split('.')[-1].title() if member.activity else 'No Activity'} {member.activity.name if member.activity else ''}"
        member_created_at = int(member.created_at.replace(tzinfo=timezone.utc).timestamp())
        member_joined_at = int(member.joined_at.replace(tzinfo=timezone.utc).timestamp())
        if member.is_avatar_animated() is True:
            member_has_nitro = True
        else:
            member_has_nitro = False

        # --------------- Image ----------------------
        #print('image gen started')
        name = member_name
        pfp = member.avatar_url_as(size=256)
        #print('pfp got')
        data = BytesIO(await pfp.read())
        pfp = Image.open(data).convert("RGBA")
        #print('pfp read')
        base = Image.open("Pictures/base.jpg").convert("RGBA")
        name = f"{name[:16]}..." if len(name) > 16 else name
        #print('base opened name got')
        date = f"Joined At: {member.joined_at.strftime('%d/%m/%Y')}"
        draw = ImageDraw.Draw(base)
        #print('date got got drawing started')
        pfp = circle(pfp)
        font = ImageFont.truetype(r"Fonts/ZenDots-Regular.ttf", 30)
        fontdate = ImageFont.truetype(r"Fonts/ZenDots-Regular.ttf", 20)
        #print('both fonts got')
        draw.text((200, 50), name, font=font, fill="#000000")
        draw.text((200, 100), date, font=fontdate, fill="#000000")
        base.paste(pfp, (30, 30), pfp)
        #print('base pasted...writing done')
        

        # ---------------- Embed ---------------------

        embed = discord.Embed(title=f"{member_name}'s Information", timestamp=ctx.message.created_at,
                              color=ctx.message.author.colour)
        embed.add_field(name="<:foxia:832549597892313159> Name", value=member_name, inline=True)
        embed.add_field(name="<:foxia:832549597892313159> ID", value=member_id, inline=True)
        embed.add_field(name="<:foxia:832549597892313159> Nickname", value=member_nickname, inline=True)
        embed.add_field(name="<:bot:773145401611255808> BOT?", value=is_bot, inline=True)
        embed.add_field(name="<:pepetrophy:904620360526356520> Top Role", value=member_top_role, inline=True)
        embed.add_field(name="<:pandacop:831800704372178944> Activity", value=member_activity, inline=True)
        embed.add_field(name="<a:time:906880876451876875> Created At", value=f"<t:{member_created_at}:F>\n(<t:{member_created_at}:R>)",
                        inline=True)
        embed.add_field(name="<a:time:906880876451876875> Joined At", value=f"<t:{member_joined_at}:F>\n(<t:{member_joined_at}:R>)",
                        inline=True)
        embed.add_field(name="<a:nitrobaby:836902390766108694> Nitro?*", value=member_has_nitro, inline=True)
        embed.set_footer(text="*Nitro checks are done based on the user's avatar", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=member_avatar_url)


        with BytesIO() as imgbyte:
            base.save(imgbyte, "PNG")
            imgbyte.seek(0)
            #print('done #1')
            file = discord.File(imgbyte, filename="image.png")
            embed.set_image(url="attachment://image.png")
            #print('done #2')
            await ctx.channel.send(file=file, embed=embed)
            #print('sent')


    @commands.command(name="paswdgen")
    async def password_generator(self, ctx, len: int):
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
    async def weather_details(self, ctx, *, query: str):
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
        pressure = data['main']['pressure']  # unit hPa
        humidity = data['main']['humidity']  # unit percentage
        wind_speed = data['wind']['speed']
        # print(min_temp, max_temp, pressure, humidity, wind_speed)
        country = data['sys']['country']
        city_name = data['name']

        embed = discord.Embed(title=f"⛅ {city_name}'s Weather Info", timestamp=ctx.message.created_at,
                              color=ctx.message.author.colour)
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

#     @commands.command(name='qr')
#     async def qr_code_gen(self, ctx, size, *, encode: str) -> BytesIO:
#         qr = qrcode.QRCode(
#             version=1,
#             error_correction=qrcode.constants.ERROR_CORRECT_H,
#             box_size=size,
#             border=4,
#         )
#         qr.add_data(f'{encode}')
#         qr.make(fit=True)
# 
#         img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
#         buffer_obj = BytesIO()
#         img.save(buffer_obj, 'png')
# 
#         with BytesIO() as imgbytes:
#             img.save(imgbytes, 'png')
#             imgbytes.seek(0)
#             read_image = buffer_obj.read()
#             await ctx.channel.send(
#                 file=discord.File(fp=imgbytes, filename='qrcode.png')
#             )
#         # img.show()

    # @commands.command(name='cheatsh')
    # async def cheat_sh_data(self, ctx, language:str, *, query):
    #     query = query.replace(" ", "%20")
    #     url = f"https://cheat.sh/{language}/{query}"
    #     response = requests.request("GET", url=url)
    #     await ctx.channel.send(f"```{language}\n{response.text[:1900]}```")


    @commands.command(name='sp')
    async def spotify_info(self, ctx, user:discord.Member=None):
        user = user or ctx.author
        check_spotify = next((activity for activity in user.activities if isinstance(activity, discord.Spotify)), None)
        
        if check_spotify == None:
            await ctx.channel.send(f"<:nospotify:906890136996937729> {user.name} is not listening to Spotify now!")
        else:
                # Images
            track_background_image = Image.open(r'Pictures/spotify_base.png')
            album_image = Image.open(requests.get(check_spotify.album_cover_url, stream=True).raw).convert('RGBA')
            #album_image = Image.open(r'Pictures/spotify_cover.png').convert('RGB')
            album_image = album_image.resize((285, 285))
            #album_image.show()
                # Fonts
            title_font = ImageFont.truetype(r'Fonts/Grotte-Regular.ttf', 30)
            artist_font = ImageFont.truetype(r'Fonts/Grotte-Regular.ttf', 20)
            album_font = ImageFont.truetype(r'Fonts/Grotte-Regular.ttf', 20)
            start_duration_font = ImageFont.truetype(r'Fonts/Grotte-Regular.ttf', 20)
            end_duration_font = ImageFont.truetype(r'Fonts/Grotte-Regular.ttf', 20)
            title = check_spotify.title if len(check_spotify.title)< 27 else f"{check_spotify.title[:27]}..."
            artist_text = check_spotify.artist if len(check_spotify.artist)< 41 else f"{check_spotify.artist[:41]}..."
            album = check_spotify.album if len(check_spotify.album) < 41 else f"{check_spotify.album[:41]}..."
                # Positions
            title_text_position = 152, 310
            artist_text_position = 152, 350
            album_text_position = 152, 375
            start_duration_text_position = 9, 405
            end_duration_text_position = 582,  405 

            # Draws
            draw_on_image = ImageDraw.Draw(track_background_image)
            track_background_image.paste(album_image, (150, 10))
            draw_on_image.text(title_text_position, title,'black', font=title_font)
            draw_on_image.text(artist_text_position, artist_text, 'black', font=artist_font)
            draw_on_image.text(album_text_position, f'Album - {album}', 'black', font=album_font)
            draw_on_image.text(start_duration_text_position, '0:00', 'black', font=start_duration_font)
            draw_on_image.text(end_duration_text_position,
                f"{dateutil.parser.parse(str(check_spotify.duration)).strftime('%M:%S')}",
                'black', font=end_duration_font)
        
            with BytesIO() as imgbyte:
                track_background_image.convert('RGB').save(imgbyte, "PNG")
                imgbyte.seek(0)
                file = discord.File(imgbyte, filename="image.png")
                await ctx.channel.send(file=file)
            #await ctx.channel.send(file=discord.File('spotify.png'))

    @commands.command(name='shell')
    @commands.is_owner()
    async def run_shell_cmds(self, ctx, *, cmd: str):
        process = await asyncio.create_subprocess_shell(
            cmd, stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()

        if stdout:
            await ctx.channel.send(f"```[stdout]\n{stdout.decode()[:1800]}```")
        if stderr:
            await ctx.channel.send(f"```[stderr]\n{stderr.decode()[:1800]}```")


    @commands.command(name='mconv')
    async def money_coverter(self, ctx, base: str, target: str, amount=100):
        c = CurrencyConverter()
        amount = int(amount)
        try:
            value = c.convert(amount, base.upper(), target.upper())
            await ctx.reply(
                f'<a:moneyfly:871972801538584596> I have converted **{amount} {base.upper()}** to {target.upper()} and the value is **{value.__format__("0.2f")} {target.upper()}**')
        except ValueError:
            await ctx.reply(
                '<:wrong:773145931973525514> Oops! One of your currency values does not exists. Do `mconvlist` to find all the valid currencies.')

    @commands.command(name='mconvlist')
    async def money_converter_list(self, ctx):
        c = CurrencyConverter()
        set_curr = "\n".join(f"{num}. {val}" for num, val in enumerate(c.currencies))
        embed = discord.Embed(title="Supported Currencies", description=f'```py\n{set_curr}```',
                              timestamp=ctx.message.created_at, colour=discord.Colour.dark_blue())

        embed.set_thumbnail(
            url="https://www.investopedia.com/thmb/lqOcGlE7PI6vLMzhn5EDdO0HvYk=/1337x1003/smart/filters:no_upscale()/GettyImages-1054017850-7ef42af7b8044d7a86cfb2bff8641e1d.jpg")

        await ctx.reply(embed=embed)

    # Error Handlers
    @user_profileimage.error
    async def user_profileimage_error_handling(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Member Not Found",
                                               description="```ini\nMake sure you have run the command providing the [username]```",
                                               timestamp=ctx.message.created_at, color=discord.Color.dark_gold()))

    @movie_info.error
    async def movie_info_error_handling(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Arguments",
                                               description="```ini\nMake sure you have run the command providing the [query] parameter```",
                                               timestamp=ctx.message.created_at, color=discord.Color.blurple()))

    @member_info_command.error
    async def member_info_error_handling(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Member Not Found",
                                               description="```ini\nMake sure you have run the command providing the [username]```",
                                               timestamp=ctx.message.created_at, color=discord.Color.dark_gold()))

    @password_generator.error
    async def password_generator_error_handling(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Arguments",
                                               description="```ini\nMake sure you have run the command providing the [length] parameter```",
                                               timestamp=ctx.message.created_at, color=discord.Color.magenta()))

    @weather_details.error
    async def weather_details_error_handling(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Arguments",
                                               description="```ini\nMake sure you have run the command providing the [place] parameter```",
                                               timestamp=ctx.message.created_at, color=discord.Color.magenta()))

    @money_coverter.error
    async def money_converter_error_handling(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            embed = discord.Embed(title="<:hellno:871582891585437759> Command Invoke Error",
                                  description="```ini\nMake sure you have run the command providing the [current-currency] [changeto-currency] [amount]* respectively```",
                                  timestamp=ctx.message.created_at, color=discord.Color.magenta())
            embed.set_footer(text="*Amount is optional. If not specified it will be 100",
                             icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    # @qr_code_decode.error
    # async def qrdec_error_handling(self, ctx, error):
    #     if isinstance(error, commands.CommandInvokeError) or isinstance(error, IndexError):
    #         await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Arguments",
    #                                            description="```ini\nMake sure you have run the command providing the [attachment].```",
    #                                            timestamp=ctx.message.created_at, color=discord.Color.magenta()))

    # @qr_code_gen.error
    # async def qrcodegen_error_handling(self, ctx, error):
    #     if isinstance(error, commands.MissingRequiredArgument):
    #         await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Arguments",
    #                                            description="```ini\nMake sure you have run the command providing the [barcode-size] [text-to-encode] parameters respectively.```",
    #                                            timestamp=ctx.message.created_at, color=discord.Color.magenta()))


def setup(client):
    client.add_cog(Utilities(client))
