# Coding=UTF8
# !python3
# /usr/bin/env python3

import discord, random
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="predict")
    async def predict(self, ctx, *, question:str):
        responses = [
            "yes", "ok", "i don't know", "no", "absolutely not"
        ]

        await ctx.channel.send(f"{random.random(responses)}")


    

def setup(client):
    client.add_cog(Fun(client))