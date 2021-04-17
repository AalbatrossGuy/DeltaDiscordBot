# Coding=UTF8
# !python
# !/usr/bin/env python3

import discord
from discord.ext import commands
from GoogleNews import GoogleNews


class NewsApi(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="gnews")
    async def google_news_api(self, ctx, period: str = '1d', *, query: str):
        global links
        global texts
        googlenews = GoogleNews(lang='en', period=period)

        googlenews.search(query)

        # onlylinks = [x for x in googlenews.get_links()]
        for i in googlenews.get_news():
            texts = [i]

        for i in googlenews.get_links():
            links = [i]

        template = [f"[{texts[x]}]({links[y]}) " for x, y in (texts, links)]
        final = [combi for combi in template]
        embed = discord.Embed(title="Test")
        embed.add_field(
            name=f"Results for {query}",
            value=f"{str(*final)}")
        await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(NewsApi(client))
