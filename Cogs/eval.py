# Coding=UTF8
# !python3
# !/usr/bin/env python3 

import discord, json, os
from discord.ext import commands
import io, contextlib, textwrap, requests, re
from pistonapi import PistonAPI


langs = json.loads(requests.get('https://emkc.org/api/v2/piston/runtimes').text)

"""this code below fetches all the available languages by calling the api. It is recommended to run this code once in a week."""
#with open('languages.json', 'w') as file:
    #file.write(json.dumps(langs))

# read collected langs and versions 
langs = json.loads(open('languages.json').read())

def check_language_and_alias(lang_call):
    latest = []
    for lang in langs:
        if (lang['language'] == lang_call) or (lang_call in lang['aliases']):
            latest.append(lang['version'])

            json_body = {
                "language": lang['language'],
                "version": ''.join(max([latest]))
            }
            
            return json.dumps(json_body)


class Eval(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="run")
    async def evaluate_code(self, ctx, lang, *, code):
        piston = PistonAPI()
        pattern = "`{3}([\w]*)\n([\S\s]+?)\n`{3}"
        regex = re.compile(pattern)
        stdin = re.findall(regex, code)[0][1]
        matchlanguage = check_language_and_alias(lang)
        try:
            matchlanguage = json.loads(matchlanguage)
        except TypeError:
            await ctx.channel.send(f"<:wrong:773145931973525514> No Language Found Of The Name, `{lang}`")
        #print(matchlanguage) for debugging purpose
        embed = discord.Embed(title="Code Output", color=discord.Color.dark_red(), timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://i.pinimg.com/originals/41/ff/08/41ff08e482a4314896060bebbe40c46e.jpg")
        embed.add_field(name="Language", value=f"`{matchlanguage['language']}`", inline=True)
        embed.add_field(name="Version", value=f"`v{matchlanguage['version']}`", inline=True)
        embed.add_field(name="<a:parrot_dance:852147639373135872> Code Output", value=f"```{piston.execute(language=matchlanguage['language'], version=matchlanguage['version'], code=stdin)}```", inline=False)
        await ctx.send(embed=embed)
        fp = "languages.json" 
        #os.remove(fp)

    @evaluate_code.error 
    async def run_error_handling(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Arguments", description="```ini\nMake sure you have ran the command using the arguments, [lang] and [code]```", timestamp=ctx.message.created_at, color=discord.Color.dark_green()))


def setup(client):
    client.add_cog(Eval(client))
