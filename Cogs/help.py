# Coding=UTF8
# !python
# !/usr/bin/env python3

import discord
from discord.ext import commands


class HelpMsg(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        # Decorators

        embed = discord.Embed(title="Help Message", colour=discord.Colour.dark_red(),
                              description=f"Type `help <command>` for getting further\ninformation on a command.",
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Content

        embed.add_field(name="<:foxia:832549597892313159> General", value="`ping`, `avatar`, `link`", inline=False)
        embed.add_field(name="⚒️  Settings",
                        value="`cp`, `set_welcomemsg`, `update_welcomemsg`, `set_leavemsg`, `update_leavemsg`",
                        inline=True)
        embed.add_field(name="📸 Image Manipulation",
                        value="`bw_u`, `negative_u`, `blur_u`, `bw_f`, `negative_f`, `blur_f`")
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
                        value="Set a new prefix for the bot or mention the bot\nto use it's commands.")
        embed.add_field(name="Example",
                        value="```yaml\n*cp &```")
        await ctx.send(embed=embed)

    @help.command()
    async def set_welcomemsg(self, ctx):
        # Decorators

        embed = discord.Embed(title="Set WelcomeMessage", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> set_welcomemsg <channel_id> <true/false>",
                        value="Use this command to set welcome message to on and off. give the channel id and ur choice.\nEither `true` or `false`.\n USE THIS COMMAND ONLY ONCE!")
        embed.add_field(name="Example",
                        value="```yaml\n*set_welcomemsg <channel_id> true/false```")
        await ctx.send(embed=embed)

    @help.command()
    async def update_welcomemsg(self, ctx):
        # Decorators

        embed = discord.Embed(title="Update WelcomeMessage", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> update_welcomemsg  <true/false>",
                        value="Use this command to update ur choice for the welcome msg. Just give either true or false if u want to switch on/off welcome message respectively. You have to first set leavemsg before using this command.")
        embed.add_field(name="Example",
                        value="```yaml\n*update_welcomemsg true\n\tOR\n*update_welcomemsg false```")

        await ctx.send(embed=embed)

    @help.command()
    async def set_leavemsg(self, ctx):
        # Decorators

        embed = discord.Embed(title="Set LeaveMessage", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> set_leavemsg <channel_id>  <true/false>",
                        value="Use this command to set leave message. Do *set_leavemsg and then give the channel id and then your option. USE THIS COMMAND ONLY ONCE!")

        embed.add_field(name="Example",
                        value="```yaml\n*set_leavemsg <channel_id> <true/false>```")

        await ctx.send(embed=embed)

    @help.command()
    async def update_leavemsg(self, ctx):
        # Decorators

        embed = discord.Embed(title="Update LeaveMessage", colour=discord.Colour.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Context

        embed.add_field(name="<a:typing:773870195336937532> update_leavemsg <channel_id>  <true/false>",
                        value="Use this command to update leave message. Just give either true or false if u want to switch on/off leave message respectively. You have to first set leavemsg before using this command.")

        embed.add_field(name="Example",
                        value="```yaml\n*set_leavemsg <channel_id> <true/false>```")

        await ctx.send(embed=embed)

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


def setup(client):
    client.add_cog(HelpMsg(client))
