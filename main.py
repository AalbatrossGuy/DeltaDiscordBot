# Coding=UTF8
# !python3
# !/usr/bin/env python3
# main.py

import discord, os, time
from discord.ext import commands
from datetime import timedelta
from decouple import config
from lib import db
from time import perf_counter

start_time = time.time()


def get_prefix(bot, message):
    prefix = db.field("SELECT Prefix FROM guilds WHERE GuildID = ?", message.guild.id)
    #bot.process_commands(message)
    
    return commands.when_mentioned_or(prefix)(bot, message)
    


Token = config('TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = commands.AutoShardedBot(command_prefix=get_prefix, case_insensitive=True,
                                 intents=intents)

client.remove_command('help')


@client.event
async def on_guild_join(guild):
    db.execute("INSERT OR IGNORE INTO guilds(GuildID) VALUES(?)", guild.id)
    db.commit()
    print("new server joined!")


@client.event
async def on_guild_remove(guild):
    db.execute("DELETE FROM guilds WHERE GuildID = ? ", guild.id)
    db.commit()


@client.command(name="cp")
@commands.has_permissions(manage_guild=True)
async def change_prefix(ctx, new_prefix):
    if len(new_prefix) > 6:
        await ctx.send("<:wrong:773145931973525514> The prefix cannot be more than 6 letters!")
    else:
        await ctx.send(f"Prefix changed to `{new_prefix}` successfully!")
        db.execute("UPDATE guilds SET Prefix = ? WHERE GuildID = ?", new_prefix, ctx.guild.id)
        db.commit()


# @client.event
# async def on_member_join(ctx):
#     db.execute("INSERT OR IGNORE INTO guilds(GuildID, Prefix) VALUES(?, ?)", int(ctx.guild.id), str(get_prefix))
#     db.commit()

@commands.is_owner()
@client.command(name="restart")
async def restart(ctx):
    await ctx.channel.send("<:exit:773159538961416222> Restarting in 5s...")
    await ctx.message.add_reaction('<:correct:773145931859886130>')
    await client.close()

@client.command(name="ping")
async def pingme(ctx):
    # ws ping
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(timedelta(seconds=difference))
    embed = discord.Embed(title=':ping_pong: Ping', color=discord.Colour.dark_gold(), timestamp=ctx.message.created_at)
    embed.add_field(name=":green_heart: `WS Ping`", value=f"{round(client.latency * 1000)}ms")

    # DB ping

    start = perf_counter()
    db.field("SELECT Prefix FROM guilds WHERE GuildID = ?", ctx.guild.id)
    end = perf_counter()
    db_ping_time = end - start
    db_ping = db_ping_time * 1000
    embed.add_field(name=":green_heart: `DB Ping`", value=f"{db_ping.__format__('0.2f')}ms")
    embed.set_footer(text="Delta Δ is the fourth letter of the Greek Alphabet", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://i.gifer.com/fyMe.gif")
    await ctx.channel.send(embed=embed)


@client.command()
async def load_extension(ctx, extension):
    client.load_extension(f'Cogs.{extension}')


@client.command()
async def unload_extension(ctx, extension):
    client.unload_extension(f'Cogs.{extension}')


for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'Cogs.{filename[:-3]}')

client.run(Token)
