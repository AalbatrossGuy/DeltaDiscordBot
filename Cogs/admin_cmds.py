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
    async def delete_channel_messages(self, ctx, limit: int=10):
        await ctx.channel.purge(limit=limit + 1)
        await ctx.channel.send(f"<:salute:831807820118622258> Purged {limit} messages!")
        await asyncio.sleep(2)
        await ctx.channel.purge(limit=1)

    @commands.has_permissions(kick_members=True)
    @commands.command(name="kick")
    async def kick_user(self, ctx, member: discord.Member):
        await member.kick()
        await ctx.message.delete()
        await ctx.channel.send(f"<:pandacop:831800704372178944> Kicked {member.mention} successfully!")

    @commands.has_permissions(ban_members=True)
    @commands.command(name="ban")
    async def ban_user(self, ctx, member: discord.Member):
        await member.ban()
        #await ctx.channel.purge(limit=1)
        await ctx.message.delete()
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
    async def purge_error_handling(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.channel.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Permissions", description="```prolog\nYou must have the Manage Messages permission to use that command!```", timestamp=ctx.message.created_at, color=discord.Color.blue()))

    @kick_user.error
    async def kick_error_handling(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Permissions", description="```prolog\nYou must have the Kick Members permission to use that command!```", timestamp=ctx.message.created_at, color=discord.Color.magenta()))

        if isinstance(error, commands.MemberNotFound):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Member Not Found", description="```ini\nSorry, the [member] you provided does not exists in the server.```"))

    @ban_user.error
    async def ban_error_handling(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Permissions", description="```prolog\nYou must have the Ban Members permission to use that command!```"), timestamp=ctx.message.created_at, color=discord.Color.greyple())
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Member Not Found", description='```ini\nSorry, the [member] you provided does not exists in the server.```', timestamp=ctx.message.created_at, color=discord.Color.blurple()))

    @unban_user.error
    async def ban_error_handling(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759>  Missing Permissions", description='```prolog\nYou must have the Ban Members permission to use that command!```', timestamp=ctx.message.created_at, color=discord.Color.gold()))


    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    @commands.command(name="lockdown")
    async def lockdown(self, ctx):
        await ctx.send(ctx.channel.name + " has been locked.")
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        

    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    @commands.command(name="unlock")
    async def unlock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send(ctx.channel.name + " has been unlocked.")
        
    @lockdown.error
    async def lockdown_error_handling(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Permissions", description="```prolog\nYou must have the Manage Channels permission to use that command!```", timestamp=ctx.message.created_at, color=discord.Color.dark_grey()))

    @unlock.error
    async def unlock_error_handling(self, error, ctx):
        if isinstance(error, commands.MissingPermissions):
            await ctx.channel.send(embed=discord.Embed(title="<:hellno:871582891585437759> Missing Permissions", description="```prolog\nYou must have the Manage Channels permission to use that command!", timestamp=ctx.message.created_at, color=discord.Color.dark_orange()))

def setup(client):
    client.add_cog(AdminCmds(client))
