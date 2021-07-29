# Coding=UTF8
# !python
# !/usr/bin/env python3

import discord
from discord.ext import commands
from lib import db


class HelpMsg(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        # Decorators
        prefix = db.field("SELECT Prefix FROM guilds WHERE GuildID = ?", ctx.message.guild.id)
        embed = discord.Embed(title="Help Message", colour=discord.Colour.dark_red(),
                              description=f"Server Prefix: `{prefix}`\nType `help <command>` for getting further\ninformation on a command.",
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Content

        embed.add_field(name="<:foxia:832549597892313159> General", value="`ping`, `say`, `avatar`, `link`, `sinfo`, `meminfo`, `socials`",
                        inline=True)
        embed.add_field(name="<:admin:852022714054869013> Admin Commands", 
                        value="`purge`, `kick`, `ban`, `unban`, `lockdown`, `unlock`")
        embed.add_field(name="📸 Image Manipulation",
                        value="`bw_u`, `negative_u`, `blur_u`, `bw_f`, `negative_f`, `blur_f`, `wasted`, `trigger`, `magic`, `pixel`, `angel`, `devil`, `windel`, `hitler`, `stringify`")
        
        embed.add_field(name="⚒️  Settings",
                        value="`cp`, `set_webhook`, `delete_webhook`",
                        inline=True)
        embed.add_field(name="<:owo:773057515826708501> Utilities",
                        value="`qr`, `qrdec`, `paswdgen`, `minfo`, `wcheck`, `run`",
                        inline=True)
        embed.add_field(name="📊 Charts <beta>",
                        value="`hbchart`, `more coming soon`")
        await ctx.send(embed=embed)

    @help.command()
    async def ping(self, ctx):
        # Decorators

        embed = discord.Embed(title="Ping", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> Ping", value="Returns the latency of the bot.")
        await ctx.send(embed=embed)

    @help.command()
    async def cp(self, ctx):
        # Decorators

        embed = discord.Embed(title="Change Prefix", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> cp <new_prefix>",
                        value="Set a new prefix for the bot or mention the bot\nto use it's commands. You must have the `Manage Server` permission to run this command.")
        embed.add_field(name="Example",
                        value="```yaml\n*cp &```")
        await ctx.send(embed=embed)

    # @help.command()
    # async def set_welcomemsg(self, ctx):
    #     # Decorators

    #     embed = discord.Embed(title="Set WelcomeMessage", colour=discord.Colour.dark_gold(),
    #                           timestamp=ctx.message.created_at)
    #     embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
    #     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

    #     # Context

    #     embed.add_field(name="<a:typing:773870195336937532> set_welcomemsg <channel_id> <true/false>",
    #                     value="Use this command to set welcome message to on and off. give the channel id and ur choice.\nEither `true` or `false`.\n USE THIS COMMAND ONLY ONCE!")
    #     embed.add_field(name="Example",
    #                     value="```yaml\n*set_welcomemsg <channel_id> true/false```")
    #     await ctx.send(embed=embed)

    # @help.command()
    # async def update_welcomemsg(self, ctx):
    #     # Decorators

    #     embed = discord.Embed(title="Update WelcomeMessage", colour=discord.Colour.dark_gold(),
    #                           timestamp=ctx.message.created_at)
    #     embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
    #     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

    #     # Context

    #     embed.add_field(name="<a:typing:773870195336937532> update_welcomemsg  <true/false>",
    #                     value="Use this command to update ur choice for the welcome msg. Just give either true or false if u want to switch on/off welcome message respectively. You have to first set leavemsg before using this command.")
    #     embed.add_field(name="Example",
    #                     value="```yaml\n*update_welcomemsg true\n\tOR\n*update_welcomemsg false```")

    #     await ctx.send(embed=embed)

    # @help.command()
    # async def set_leavemsg(self, ctx):
    #     # Decorators

    #     embed = discord.Embed(title="Set LeaveMessage", colour=discord.Colour.dark_gold(),
    #                           timestamp=ctx.message.created_at)
    #     embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
    #     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

    #     # Context

    #     embed.add_field(name="<a:typing:773870195336937532> set_leavemsg <channel_id>  <true/false>",
    #                     value="Use this command to set leave message. Do *set_leavemsg and then give the channel id and then your option. USE THIS COMMAND ONLY ONCE!")

    #     embed.add_field(name="Example",
    #                     value="```yaml\n*set_leavemsg <channel_id> <true/false>```")

    #     await ctx.send(embed=embed)

    # @help.command()
    # async def update_leavemsg(self, ctx):
    #     # Decorators

    #     embed = discord.Embed(title="Update LeaveMessage", colour=discord.Colour.dark_gold(),
    #                           timestamp=ctx.message.created_at)
    #     embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
    #     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

    #     # Context

    #     embed.add_field(name="<a:typing:773870195336937532> update_leavemsg <channel_id>  <true/false>",
    #                     value="Use this command to update leave message. Just give either true or false if u want to switch on/off leave message respectively. You have to first set leavemsg before using this command.")

    #     embed.add_field(name="Example",
    #                     value="```yaml\n*set_leavemsg <channel_id> <true/false>```")

    #     await ctx.send(embed=embed)

    @help.command()
    async def avatar(self, ctx):
        # Decorators

        embed = discord.Embed(title="Avatar", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> avatar <user_name>",
                        value="Use this command to see the avatar of a user. You can either type the user's name or use his id or ping him to get the result. If only `*avatar` is done then the author's image will be returned")

        embed.add_field(name="Example",
                        value="```yaml\n*avatar\n\tOR\n*avatar AalbatrossGuy\n\tOR\n*avatar <user_id>\n\tOR\n*avatar @AalbatrossGuy```")

        await ctx.send(embed=embed)

    @help.command()
    async def link(self, ctx):
        # Decorators

        embed = discord.Embed(title="Link", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> link",
                        value="Use this command to get the bot's invite link.")

        embed.add_field(name="Example",
                        value="```yaml\n*link```")

        await ctx.send(embed=embed)

    @help.command()
    async def bw_u(self, ctx):
        embed = discord.Embed(title="Black And White User", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> bw_u <user_name/id>",
                        value="Use this command to get a black and white image of the mentioned user's profile picture. If used without stating username/id, it will return the author's black and white image")

        embed.add_field(name="Example",
                        value="```yaml\n*bw_u AalbatrossGuy\n\tOR\n*bw_u @AalbatrossGuy\n\tOR\n*bw_u <user_id>```")

        await ctx.send(embed=embed)

    @help.command()
    async def negative_u(self, ctx):
        embed = discord.Embed(title="Negative User", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> negative_u <user_name/id>",
                        value="Use this command to get a negative image of the mentioned user's profile picture. If used without stating username/id, it will return the author's negative image")

        embed.add_field(name="Example",
                        value="```yaml\n*negative_u AalbatrossGuy\n\tOR\n*negative_u @AalbatrossGuy\n\tOR\n*negative_u <user_id>```")

        await ctx.send(embed=embed)

    @help.command()
    async def blur_u(self, ctx):
        embed = discord.Embed(title="Blur User", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> blur_u <radius> <user_name/id>",
                        value="Use this command to get a blurred image of the mentioned user's profile picture. State the radius of the blur between 1-10 If used without stating username/id, it will return the author's blurred image")

        embed.add_field(name="Example",
                        value="```yaml\n*blur_u 5 AalbatrossGuy\n\tOR\n*blur_u 2 @AalbatrossGuy\n\tOR\n*blur_u 10 <user_id>```")

        await ctx.send(embed=embed)

    @help.command()
    async def bw_f(self, ctx):
        embed = discord.Embed(title="Black And White File", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> bw_f",
                        value="Attach an image and use this command to get the black and white version of it. If you don't know how to, then [click here](https://support.discord.com/hc/en-us/articles/211866427-How-do-I-upload-images-and-GIFs-#:~:text=The%20first%20way%20to%20upload,That%20simple!)")

        embed.add_field(name="Example",
                        value="```yaml\n*bw_f <with the attached image>```")

        await ctx.send(embed=embed)

    @help.command()
    async def negative_f(self, ctx):
        embed = discord.Embed(title="Negative File", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> negative_f",
                        value="Attach an image and use this command to get the negative version of it. If you don't know how to, then [click here](https://support.discord.com/hc/en-us/articles/211866427-How-do-I-upload-images-and-GIFs-#:~:text=The%20first%20way%20to%20upload,That%20simple!)")

        embed.add_field(name="Example",
                        value="```yaml\n*negative_f <with the attached image>```")
        await ctx.send(embed=embed)

    @help.command()
    async def blur_f(self, ctx):
        embed = discord.Embed(title="Blur File", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> blur_f <radius>",
                        value="Attach an image and use this command to get the blurred version of it. The radius must be mentioned and should be between 1-10. If you don't know how to attach an image, then [click here](https://support.discord.com/hc/en-us/articles/211866427-How-do-I-upload-images-and-GIFs-#:~:text=The%20first%20way%20to%20upload,That%20simple!)")

        embed.add_field(name="Example",
                        value="```yaml\n*blur_f <radius between 1-10> <with the attached image>```")
        await ctx.send(embed=embed)

    @help.command()
    async def say(self, ctx):
        embed = discord.Embed(title="Say", colour=discord.Colour.dark_gold(),
                        timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> say <message>",
                        value="Use this command to make the bot repeat the <message>. Make sure that the webhook is already set for this channel. For more info do `set_webhook`")

        embed.add_field(name="Example",
                       value="```yaml\n*say \n*say <message>```")
        await ctx.send(embed=embed)

    @help.command()
    async def set_webhook(self, ctx):
        embed = discord.Embed(title="Set Webhook", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> set_webhook",
                        value="Use this command to set the webhook for the respective channel. You cannot use the say command before setting the channel_id")

        embed.add_field(name="Example",
                        value="```yaml\n*set_webhook```")
        await ctx.send(embed=embed)

    @help.command()
    async def delete_webhook(self, ctx):
        embed = discord.Embed(title="Delete Webhook", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> delete_webhook",
                       value="Use this command to delete the webhook for the respective channel.\nNOTE: This command only deletes the channel_id from the database. To manually delete the webhook from the channel go to edit channel > integrations > view webhook and tselect the with `SayCmd Webhook`")

        embed.add_field(name="Example",
                       value="```delete_webhook```")
        await ctx.send(embed=embed)

    @help.command()
    async def minfo(self, ctx):
        embed = discord.Embed(title="Movie Info", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> minfo <movie_name>",
                        value="Use this command to search for a movie and get it's details")

        embed.add_field(name="Example",
                        value="```minfo Avengers```")
        await ctx.send(embed=embed)

    @help.command()
    async def meminfo(self, ctx):
        embed = discord.Embed(title="Member Info", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> meminfo <username/user_id/@usermention>",
                        value="Use this command to get information about a user by either typing their name or their ID or mentioning them.")

        embed.add_field(name="Example",
                        value="```meminfo Delta Δ```")
        await ctx.send(embed=embed)

    @help.command()
    async def sinfo(self, ctx):
        embed = discord.Embed(title="Server Info", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> sinfo",
                        value="Use this command to get information about the server you are in.")

        embed.add_field(name="Example",
                        value="```meminfo Delta Δ```")
        await ctx.send(embed=embed)

    @help.command()
    async def wcheck(self, ctx):
        embed = discord.Embed(title="Weather Info", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> sinfo",
                        value="Use this command to get information about a place anywhere in the world.")

        embed.add_field(name="Example",
                        value="```wcheck iceland```")
        await ctx.send(embed=embed)

    @help.command()
    async def paswdgen(self, ctx):
        embed = discord.Embed(title="Password Generator", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> paswdgen <len>",
                        value="Use this command to get a randomly generated password of size <len>. The value of <len> must be less than 60.")

        embed.add_field(name="Example",
                        value="```paswdgen 10```")
        await ctx.send(embed=embed)

    @help.command()
    async def qr(self, ctx):
        embed = discord.Embed(title="QR Code Generator", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> qr <size> <text>",
                        value="Use this command to generate a qrcode based on your text. The <size> parameter takes a number and decides the size of the QR image. The second parameter, i.e, <text> takes the actual message to encode.")

        embed.add_field(name="Example",
                        value="```qr 10 Hello World.```")
        await ctx.send(embed=embed)

    @help.command()
    async def qrdec(self, ctx):
        embed = discord.Embed(title="QR Code Decoder", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> sinfo",
                        value="Use this command to decode a qr code. Make sure u attach the image of the qrcode as a discord attachment.")

        embed.add_field(name="Example",
                        value="```qrdec <file-attached>```")
        await ctx.send(embed=embed)

    @help.command()
    async def hbchart(self, ctx):
        embed = discord.Embed(title="Horizontal Bar Chart", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> hbchart <data>",
                        value="Use this command to generate a horizontal bar chart. The numbers must be seperated by a ' | '. The character must contain a space before and after of it '<space>|<space>'. The first set of numbers before the `|` is for x axis and the later part is for y axis.Each numbers must also be seperated by space. You can insert any kind of data in the chart as long as it is equal on both the axes.")
        embed.add_field(name="Note", value="```The numbers before and after the '|' must be of equal length. E.g - 1 2 3 4 | 8 7 9 8 <:correct:773145931859886130>\n1 2 3 4 | 2 4 3 <:wrong:773145931973525514>```")

        embed.add_field(name="Example",
                        value="```hbchart 1 2 3 | 8 6 7 4```")
        await ctx.send(embed=embed)

    @help.command()
    async def purge(self, ctx):
        embed = discord.Embed(title="Clear Messages", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> purge <limit>",
                        value="Use this command to delete <limit> number of message(s). You must have the `Manage Messages` permission to perform this command.")

        embed.add_field(name="Example",
                        value="```purge 20```")
        await ctx.send(embed=embed)

    @help.command()
    async def kick(self, ctx):
        embed = discord.Embed(title="Kick Member", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> kick <member>",
                        value="Use this command to kick <member>. You must have the `Kick Members` permission to perform this command. You can either mention the user to kick or just write their name or use their id. All of them will be valid.")


        embed.add_field(name="Example",
                        value="```kick @User <user-mention>\nkick User <user-name>\nkick 19298402018402 <user-id>```")
        await ctx.send(embed=embed)

    @help.command()
    async def ban(self, ctx):
        embed = discord.Embed(title="Ban Member", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> ban <member>",
                        value="Use this command to ban <member>. You must have the `Ban Members` permission to perform this command. You can either mention the user to ban or just write their name or use their id. All of them will be valid.")


        embed.add_field(name="Example",
                        value="```ban @User <user-mention>\nban User <user-name>\nban 19298402018402 <user-id>```")
        await ctx.send(embed=embed)

    @help.command()
    async def unban(self,ctx):
        embed = discord.Embed(title="Unban Member", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> unban <member>",
                        value="Use this command to unban <member>. You must have the `Ban Members` permission to perform this command. You have to provide the member name along with their discriminator.")


        embed.add_field(name="Example",
                        value="```unban User#2120```")
        await ctx.send(embed=embed)

    @help.command()
    async def lockdown(self, ctx):
        embed = discord.Embed(title="Lockdown A Channel", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> lockdown",
                        value="Use this command to lock the channel in which it has been executed. You must have the `Manage Channels` permission to perform this command.")
        
        embed.add_field(name="Example",
                        value="```lockdown```")
        await ctx.send(embed=embed)

    @help.command()
    async def unlock(self, ctx):
        embed = discord.Embed(title="Unlock A Channel", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> unlock",
                        value="Use this command to unlock the channel where this command is executed. You must have the `Manage Channels` permission to perform this command.")


        embed.add_field(name="Example",
                        value="```unlock```")
        await ctx.send(embed=embed)

    @help.command()
    async def run(self, ctx):
        embed = discord.Embed(title="Evaluate Your Code", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> run <language> <code-in-codeblocks>",
                        value="Use this command to run on your code in discord itself. The proper format for running this command is - run <language> \```[syntax] <new-line> your-code-here```. The bot uses the [piston api](https://github.com/engineer-man/piston#Public-API) for running the codes you provide. The bot currently supports 51 languages. To view them, [click here](https://drive.google.com/file/d/1oEsJkgfPOzWig9PWnncIDbfuSmo93JFt/view?usp=sharing)")

        await ctx.send(embed=embed)

    @help.command()
    async def socials(self, ctx):
        embed = discord.Embed(title="Author's Socials", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> socials",
                        value="Use this command to view the socials of the author of the bot.")


        embed.add_field(name="Example",
                        value="```socials```")
        await ctx.send(embed=embed)

    @help.command()
    async def wasted(self, ctx):
        embed = discord.Embed(title="Wasted", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> wasted <member-name/id/mention>",
                        value="Use this command to get the wasted overlay to the member's profile picture. You can either mention the member or use his id or just type his name. If no member name is provided, then the bot takes the profile picture of the author.")


        embed.add_field(name="Example",
                        value="```wasted <member-name/id/mention>```")
        await ctx.send(embed=embed)

    @help.command()
    async def trigger(self, ctx):
        embed = discord.Embed(title="Trigger", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> trigger <member-name/id/mention>",
                        value="Use this command to get the triggered overlay to the member's profile picture. You can either mention the member or use his id or just type his name. If no member name is provided, then the bot takes the profile picture of the author.")


        embed.add_field(name="Example",
                        value="```trigger <member-name/id/mention>```")
        await ctx.send(embed=embed)

    @help.command()
    async def magic(self, ctx):
        embed = discord.Embed(title="Magic", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> magic <member-name/id/mention>",
                        value="Use this command to get the magik overlay to the member's profile picture. You can either mention the member or use his id or just type his name. If no member name is provided, then the bot takes the profile picture of the author.")


        embed.add_field(name="Example",
                        value="```magic <member-name/id/mention>```")
        await ctx.send(embed=embed)

    @help.command()
    async def pixel(self, ctx):
        embed = discord.Embed(title="Pixelate", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> wasted <member-name/id/mention>",
                        value="Use this command to pixelate the member's profile picture. You can either mention the member or use his id or just type his name. If no member name is provided, then the bot takes the profile picture of the author.")


        embed.add_field(name="Example",
                        value="```pixel <member-name/id/mention>```")
        await ctx.send(embed=embed)

    @help.command()
    async def angel(self, ctx):
        embed = discord.Embed(title="Angel", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> angel <member-name/id/mention>",
                        value="Use this command to get the angel overlay to the member's profile picture. You can either mention the member or use his id or just type his name. If no member name is provided, then the bot takes the profile picture of the author.")


        embed.add_field(name="Example",
                        value="```angel <member-name/id/mention>```")
        await ctx.send(embed=embed)

    @help.command()
    async def devil(self, ctx):
        embed = discord.Embed(title="Devil", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> devil <member-name/id/mention>",
                        value="Use this command to get the devil overlay to the member's profile picture. You can either mention the member or use his id or just type his name. If no member name is provided, then the bot takes the profile picture of the author.")


        embed.add_field(name="Example",
                        value="```devil <member-name/id/mention>```")
        await ctx.send(embed=embed)

    @help.command()
    async def windel(self, ctx):
        embed = discord.Embed(title="Windows Delete", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> windel <member-name/id/mention>",
                        value="Use this command to get the windows delete overlay to the member's profile picture. You can either mention the member or use his id or just type his name. If no member name is provided, then the bot takes the profile picture of the author.")


        embed.add_field(name="Example",
                        value="```windel <member-name/id/mention>```")
        await ctx.send(embed=embed)

    @help.command()
    async def hitler(self, ctx):
        embed = discord.Embed(title="Hitler", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> hitler <member-name/id/mention>",
                        value="Use this command to get the `Most Dangerous Than Hitler` overlay to the member's profile picture. You can either mention the member or use his id or just type his name. If no member name is provided, then the bot takes the profile picture of the author.")


        embed.add_field(name="Example",
                        value="```hitler <member-name/id/mention>```")
        await ctx.send(embed=embed)

    @help.command()
    async def stringify(self, ctx):
        embed = discord.Embed(title="Stringify", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> stringify <member-name/id/mention>",
                        value="Use this command to the stringify the member's profile picture. You can either mention the member or use his id or just type his name. If no member name is provided, then the bot takes the profile picture of the author.")


        embed.add_field(name="Example",
                        value="```stringify <member-name/id/mention>```")
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(HelpMsg(client))
