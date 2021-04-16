# Coding=UTF8
# !python
# !/usr/bin/env python3

import discord
from discord.ext import commands


class Utilities(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="avatar")
    async def user_profileimage(self, ctx, *, member: discord.Member):
        await ctx.send(member.avatar_url)


def setup(client):
    client.add_cog(Utilities(client))
