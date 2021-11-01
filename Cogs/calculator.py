import discord, asyncio
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle
from customs.customs import Buttons, KillButtons
from datetime import datetime, timedelta

class Calculator(commands.Cog):
    def __init__(self, client):
        self.client = client 
    
    @staticmethod 
    def calculate(expr):
        x = expr.replace('x', '*')
        x = x.replace('÷', '/')
        answr = ''
        try:
            answr = str(eval(x))
        except:
            answr = "Oops! I went Brainded. Try again Later."

        return answr

    @commands.command(name='calcu')
    async def calculator(self, ctx):
        msg = await ctx.reply(content="Calculator is Starting...")
        await asyncio.sleep(1.0)
        expr = '```None```'
        deathEmbed = discord.Embed(title="<a:alienalien:870611180232769596> Wasted!",
                                   description="Your calculator's ded. Sadly it's battery lasts only for 3 minutes. Try creating another calculator.")
        deathEmbed.set_thumbnail(url='https://i.ytimg.com/vi/mm1EGefKyqY/maxresdefault.jpg')
        tdelta = datetime.utcnow() + timedelta(minutes=3)
        embed = discord.Embed(title=f"<:calculator:870610558188126229> {ctx.author.name}'s Personal Calculator",
                              description=expr, timestamp=tdelta, color=discord.Color.dark_magenta())
        await msg.edit(
            content='', components=Buttons, embed=embed
        )
        # <a:alienalien:870611180232769596> Your Calculator is now Dead.
        try:
            while msg.created_at < tdelta:
                res = await self.client.wait_for('button_click', timeout=180)
                if res.author.id == ctx.author.id and res.message.embeds[0].timestamp < tdelta:
                    expr = f"{res.message.embeds[0].description}".replace("`", '')
                    # print(expr)
                    if expr == 'None' or expr == "Oops! I went Brainded. Try again Later.":
                        expr = ''
                    if res.component.label == 'Quit':
                        await res.respond(
                            content='<a:alienalien:870611180232769596> You have quit your calculator.', type=7,
                            components=KillButtons
                        )
                        break
                    elif res.component.label == '⟵':
                        expr = expr[:-1]
                    elif res.component.label == 'Clear':
                        # expr = None
                        expr = None
                    elif res.component.label == 'Answ':
                        expr = Calculator.calculate(expr)
                    else:
                        expr += res.component.label
                        # print(expr)
                    emptyembed = discord.Embed(
                        title=f"<:calculator:870610558188126229> {res.author.name} | Calculating...",
                        description=f"```{expr}```", timestamp=tdelta, color=discord.Color.dark_blue())
                    await res.respond(content='', embed=emptyembed, components=Buttons, type=7)

        except asyncio.TimeoutError:
            await ctx.reply(embed=deathEmbed)


def setup(client):
    client.add_cog(Calculator(client))
