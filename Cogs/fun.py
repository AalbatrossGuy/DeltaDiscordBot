# Coding=UTF8
# !python3
# /usr/bin/env python3

import discord
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="memes")
    async def reddit_memes(self, ctx):
        pass

    

def setup(client):
    client.add_cog(Fun(client))