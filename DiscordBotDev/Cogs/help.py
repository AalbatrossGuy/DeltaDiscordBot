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
        embed.add_field(name="⚒️  Settings", value="`cp`", inline=False)
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


def setup(client):
    client.add_cog(HelpMsg(client))
