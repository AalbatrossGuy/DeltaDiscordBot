# Coding=UTF8
# !python3
# !/usr/bin/env python3 

import discord, json, os
from discord.ext import commands
import io, contextlib, textwrap, requests, re
from pistonapi import PistonAPI

langs = json.loads(requests.get('https://emkc.org/api/v2/piston/runtimes').text)

"""this code below fetches all the available languages by calling the api. It is recommended to run this code once in a week."""
# with open('languages.json', 'w') as file:
#     file.write(json.dumps(langs))
#
# # read collected langs and versions
# langs = json.loads(open('languages.json').read())


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


def format_java(code: str):
    if 'class' in code:
        return code

    imports = []
    codes = [
        'public class boiler {public static void main(String[] args) {']

    lines = code.replace(';', ';\n').split('\n')
    for line in lines:
        if line.lstrip().startswith('import'):
            imports.append(line)
        else:
            codes.append(line)

    codes.append('\n\t}}')
    return '\n'.join(imports + codes)


# def format_c(code: str):
#     if 'main' in code:
#         return code
#
#     imports = []
#     codes = ['int main() {']
#
#     lines = code.replace(';', ';\n').split('\n')
#     for line in lines:
#         if line.lstrip().startswith('#include'):
#             imports.append(line)
#         else:
#             codes.append(line)
#     codes.append('return 0;\n}')
#     return '\n'.join(imports + codes)


def format_go(code: str):
    if 'main' in code:
        return code

    package = ['package main']
    imports = []
    codes = ['func main() {']

    lines = code.split('\n')
    for line in lines:
        if line.lstrip().startswith('import'):
            imports.append(line)
        else:
            codes.append(line)

    codes.append('}')
    return '\n'.join(package + imports + codes)


def format_c_cpp(code: str):
    if 'main' in code:
        return code

    imports = []
    codes = ['int main() {']

    lines = code.replace(';', ';\n').split('\n')
    for line in lines:
        if line.lstrip().startswith('#include'):
            imports.append(line)
        else:
            codes.append(line)

    codes.append('}')
    return '\n'.join(imports + codes)


def format_csharp(code: str):
    if 'class' in code:
        return code

    imports = []
    codes = ['class Program{']
    if not 'static void Main' in code:
        codes.append('static void Main(string[] args){')

    lines = code.replace(';', ';\n').split('\n')
    for line in lines:
        if line.lstrip().startswith('using'):
            imports.append(line)
        else:
            codes.append(line)

    if not 'static void Main' in code:
        codes.append('}')
    codes.append('}')

    return '\n'.join(imports + codes)


class Eval(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="run")
    async def evaluate_code(self, ctx, lang, *, code):
        piston = PistonAPI()
        pattern = "`{3}([\w]*)\n([\S\s]+?)\n`{3}"
        regex = re.compile(pattern)
        stdin = re.findall(regex, code)[0][1]
        # print(stdin)
        matchlanguage = check_language_and_alias(lang)
        try:
            matchlanguage = json.loads(matchlanguage)
            print(matchlanguage)
            if matchlanguage['language'] == 'java':
                # print('yes')
                stdin = format_java(stdin)
            if matchlanguage['language'] == 'c' or matchlanguage['language'] == 'cpp':
                stdin = format_c_cpp(stdin)
            if matchlanguage['language'] == 'go':
                stdin = format_go(stdin)
            if matchlanguage['language'] == 'csharp':
                stdin = format_csharp(stdin)
            else:
                stdin = stdin
        except TypeError:
            await ctx.channel.send(f"<:wrong:773145931973525514> No Language Found Of The Name, `{lang}`")
        # print(matchlanguage) for debugging purpose

        embed = discord.Embed(title="Code Output", color=discord.Color.dark_red(), timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://i.pinimg.com/originals/41/ff/08/41ff08e482a4314896060bebbe40c46e.jpg")
        embed.add_field(name="Language", value=f"`{matchlanguage['language']}`", inline=True)
        embed.add_field(name="Version", value=f"`v{matchlanguage['version']}`", inline=True)
        embed.add_field(name="<a:parrot_dance:852147639373135872> Code Output",
                        value=f"```{piston.execute(language=matchlanguage['language'], version=matchlanguage['version'], code=stdin)}```",
                        inline=False)
        await ctx.send(embed=embed)
        fp = "languages.json"
        # os.remove(fp)

    @evaluate_code.error
    async def run_error_handling(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Arguments",
                                               description="```ini\nMake sure you have ran the command using the arguments, [lang] and [code]```",
                                               timestamp=ctx.message.created_at, color=discord.Color.dark_green()))

    # @commands.command(name='cheatsh')
    # async def cheat_sh_data(self, ctx, language:str, *, query):
    #     query = query.replace(" ", "%20")
    #     url = f"https://cheat.sh/{language}/{query}"
    #     response = requests.request("GET", url=url)
    #     await ctx.channel.send(f"```{language}\n{response.text[:1900]}```")

def setup(client):
    client.add_cog(Eval(client))
