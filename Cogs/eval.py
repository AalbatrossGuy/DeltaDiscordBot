# Coding=UTF8
# !python3
# !/usr/bin/env python3 

import discord 
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
        language_tuple = ("bash", "brainfuck", "cjam", "clojure", "cobol", "coffeescript", "cow", "crystal", "dart", "dash", "deno", "dotnet", "dragon", "elixir", "emacs", "erlang", "gawk", "gcc", "go", "golfscript", "groovy",
                    "haskell", "java", "jelly", "juila", "kotlin", "lisp", "lolcode", "lua", "mono", "nasm", "nim", "node", "ocaml", "octave", "osabie", "paradoc", "pascal", "perl", "php", "ponylang", "prolog", "pure", "pyth", "python",
                    "rockstar", "ruby", "rust", "scala", "swift", "typescript", "vlang", "yeethon", "zig")

        versions_tuple = ("5.1.0", "2.7.3", "0.6.5", "1.10.3", "3.1.2", "2.5.1", "1.0.0", "0.36.1", "2.12.1", "0.5.11", "1.7.5", "5.0.201", "1.9.8", "1.11.3", "27.1.0", "23.0.0", "5.1.0", "10.2.0", "1.16.2", "1.0.0", "3.0.7", "9.0.1", "15.0.2",
                    "0.1.31", "1.5.4", "1.4.31", "2.1.2", "0.11.2", "5.4.2", "6.12.0", "2.15.5", "1.4.4", "15.10.0", "4.12.0", "6.2.0", "1.0.1", "0.6.0", "3.2.0", "5.26.1", "8.0.2", "0.39.0", "8.2.4", "0.68.0", "1.0.0", "3.9.4", "1.0.0", 
                    "3.0.1", "1.50.0", "3.0.0", "5.3.3", "4.2.3", "0.1.13", "3.10.0", "0.7.1")

        
        for language, version in zip(language_tuple, versions_tuple):
            if  lang in language:
                embed = discord.Embed(title="Code Output", color=discord.Color.dark_red(), timestamp=ctx.message.created_at)
                embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
                embed.set_thumbnail(url="https://i.pinimg.com/originals/41/ff/08/41ff08e482a4314896060bebbe40c46e.jpg")
                embed.add_field(name="Language", value=f"`{language}`", inline=True)
                embed.add_field(name="Version", value=f"`v{version}`", inline=True)
                embed.add_field(name="<a:parrot_dance:852147639373135872> Code Output", value=f"```{piston.execute(language=language, version=version, code=stdin)}```", inline=False)
                await ctx.send(embed=embed)
            

            
      

def setup(client):
    client.add_cog(Eval(client))
