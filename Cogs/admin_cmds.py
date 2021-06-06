# Coding=UTF8
# !python
# !/usr/bin/env python3

import discord
from discord.ext import commands
import asyncio


class AdminCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(manage_messages=True)
    @commands.command(name="purge", aliases=['clear', 'delete'])
    async def delete_channel_messages(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit + 1)
        await ctx.channel.send(f"<:salute:831807820118622258> Purged {limit} messages!")
        await asyncio.sleep(2)
        await ctx.channel.purge(limit=1)

    @commands.has_permissions(kick_members=True)
    @commands.command(name="kick")
    async def kick_user(self, ctx, member: discord.Member):
        await member.kick()
        await ctx.channel.purge(limit=1)
        await ctx.channel.send(f"<:pandacop:831800704372178944> Kicked {member.mention} successfully!")

    @commands.has_permissions(ban_members=True)
    @commands.command(name="ban")
    async def ban_user(self, ctx, member: discord.Member):
        await member.ban()
        await ctx.channel.purge(limit=1)
        await ctx.channel.send(f"<:pandacop:831800704372178944> Banned {member.mention} successfully!")

    @commands.has_permissions(ban_members=True)
    @commands.command(name="unban")
    async def unban_user(self, ctx, *, member):
        banned_users = await ctx.guild.bans()

        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.channel.purge(limit=1)
                await ctx.channel.send(f"<:pandacop:831800704372178944> Unbanned {user.mention} successfully!")

    @delete_channel_messages.error
    async def purge_error_handling(self, error, ctx):
        if isinstance(error, commands.MissingPermissions):
            await ctx.channel.send(
                "<:nope:735473789714038874> You must have the `Manage Messages` permission to use that command!")

    @kick_user.error
    async def kick_error_handling(self, error, ctx):
        if isinstance(error, commands.MissingPermissions):
            await ctx.channel.send(
                "<:nope:735473789714038874> You must have the `Kick Members` permission to use that command!")

    @ban_user.error
    async def ban_error_handling(self, error, ctx):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("<:nope:735473789714038874> You must have the `Ban Members` permission to use that command!")

    @unban_user.error
    async def ban_error_handling(self, error, ctx):
        if isinstance(error, commands.MissingPermissions):
            await ctx.channel.send(
                "<:nope:735473789714038874> You must have the `Ban Members` permission to use that command!")

    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    @commands.command(name="lockdown")
    async def lockdown(self, ctx):
        # await ctx.send(ctx.channel.name + " has been locked.")
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        

    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    @commands.command(name="unlock")
    async def unlock(self, ctx):
        # await ctx.send(ctx.channel.name + " has been unlocked.")
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        
        


def setup(client):
    client.add_cog(AdminCmds(client))
