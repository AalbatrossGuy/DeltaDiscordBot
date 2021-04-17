# Coding=UTF8
# !python
# !/usr/bin/env python3

import discord
from discord.ext import commands


class Utilities(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="avatar")
    async def user_profileimage(self, ctx, *, member: discord.Member = None):
        member = member or ctx.message.author
        jpg = member.avatar_url_as(format='jpg')
        webp = member.avatar_url_as(format='webp')
        png = member.avatar_url_as(format='png')

        embed = discord.Embed(title=f"Avatar of {member}", description=f"[jpg]({jpg}) | [png]({png}) | [webp]({webp})",
                              color=discord.Colour.dark_gold(), timestamp=ctx.message.created_at)
        embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
        # embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831369746855362590/831369994474094622/Logo.jpg")
        embed.set_image(url=member.avatar_url)
        await ctx.channel.send(embed=embed)

    @commands.command(name="link")
    async def send_bot_invite_link(self, ctx):
        embed = discord.Embed(title="Invite Me 🥰", timestamp=ctx.message.created_at, color=discord.Colour.dark_gold(),
                              description="Hey there! click on [this link](https://discord.com/oauth2/authorize?client_id=830047831972118588&permissions=109638&scope=bot) to invite me to your server!")
        embed.set_thumbnail(url="https://static.wixstatic.com/media/6e38f1_72944a54fe214e029653f12798bb8136~mv2.png/v1/fill/w_560,h_210,al_c,q_85,usm_0.66_1.00_0.01/6e38f1_72944a54fe214e029653f12798bb8136~mv2.webp")

        await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(Utilities(client))
