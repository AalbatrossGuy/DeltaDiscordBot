# Coding=UTF8
# !python3
# !/usr/bin/env python3 

import discord, json 
from discord.ext import commands
import io, contextlib, textwrap, requests, re
from pistonapi import PistonAPI

class Eval(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="eval")
    async def evaluate_code(self, ctx, lang, *, code):
        piston = PistonAPI()

        pattern = "`{3}([\w]*)\n([\S\s]+?)\n`{3}"
        regex = re.compile(pattern)
        stdin = re.findall(regex, code)[0][1]
        
        languages = json.loads(requests.get("https://emkc.org/api/v2/piston/runtimes").text)
        for serlang in languages:
            if  serlang['language'] == lang:
                embed = discord.Embed(title="Code Output", color=discord.Color.dark_red(), timestamp=ctx.message.created_at)
                embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
                embed.set_thumbnail(url="https://i.pinimg.com/originals/41/ff/08/41ff08e482a4314896060bebbe40c46e.jpg")
                embed.add_field(name="Language", value=f"`{serlang['language']}`", inline=True)
                embed.add_field(name="Version", value=f"`v{serlang['version']}`", inline=True)
                embed.add_field(name="<a:parrot_dance:852147639373135872> Code Output", value=f"```{piston.execute(language=serlang['language'], version=serlang['version'], code=stdin)}```", inline=False)
                await ctx.send(embed=embed)
            

            
      

def setup(client):
    client.add_cog(Eval(client))
