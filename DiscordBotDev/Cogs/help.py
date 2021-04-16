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

        embed = discord.Embed(title="Help Message", colour=discord.Colour.dark_gold(),
                              description=f"Type `help <command>` for getting further\ninformation on a command.",
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")

        # Content

        embed.add_field(name="<a:dogeparty:778838980074143744> Fun", value="`ping`", inline=False)
        embed.add_field(name="⚒️  Settings",
                        value="`cp`, `set_welcomemsg`, `update_welcomemsg`, `set_leavemsg`, `update_leavemsg`",
                        inline=False)
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
                        value="```yaml\n*update_welcomemsg true\nOR\n*update_welcomemsg false```")

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


def setup(client):
    client.add_cog(HelpMsg(client))
