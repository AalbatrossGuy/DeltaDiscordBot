import discord
from discord.ext import commands
import robloxpy, json


class GamesAPI(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="rinfo")
    async def roblox_info(self, ctx, *, username: str) -> None:
        _userid = robloxpy.User.External.GetID(username)
        if _userid == "User not found":
            embed=discord.Embed(title="<:nub:874269425505820712> Member Not Found", description=f"No member of the name {username} was found!", timestamp=ctx.message.created_at, color=discord.Color.red())
            await ctx.reply(embed=embed)
        else:  
            try:
                is_online = "true" if robloxpy.User.External.IsOnline(_userid) is True else "false"
                is_banned = "false" if robloxpy.User.External.Isbanned(_userid) is False else "true"
                desc = robloxpy.User.External.GetDescription(_userid) if len(robloxpy.User.External.GetDescription(_userid))!=0 else None
                creation_date = robloxpy.User.External.CreationDate(_userid, 1)
                image = robloxpy.User.External.GetBust(_userid)
                
                stuff = robloxpy.User.External.GetLimiteds(_userid)[0][:10]
                stuff.append("...truncated")
                truncatedone = "\n".join(stuff)

                if len(robloxpy.User.External.GetLimiteds(_userid)[0]) !=0 and len(robloxpy.User.External.GetLimiteds(_userid)[0])< 11:
                    #print(len(robloxpy.User.External.GetLimiteds(_userid)[0]))
                    #print("ran exception")
                    stuff = "\n".join(robloxpy.User.External.GetLimiteds(_userid)[0])
                elif len(robloxpy.User.External.GetLimiteds(_userid)[0]) > 11:
                    stuff = truncatedone
                else:
                    stuff = None
                friend_count = robloxpy.User.Friends.External.GetCount(_userid)
                followers = robloxpy.User.Friends.External.GetFollowerCount(_userid)

                embed=discord.Embed(title="Roblox Info", timestamp=ctx.message.created_at, color=discord.Color.dark_gold())
                embed.set_thumbnail(url=image)
                embed.set_footer(text="*names are case-sensitive!", icon_url=ctx.author.avatar_url)
                embed.set_author(name='"Roblox is SHIT" - AalbatrossGuy, 2021', icon_url='https://cdn.discordapp.com/attachments/831377063382089798/870677659032617010/static_logo_choice.png')
                embed.add_field(name="📛 Name*", value=username)
                embed.add_field(name="<:online:870496098911940718> Is Online?", value=is_online)
                embed.add_field(name="<:ban:874509148421754931> Is Banned?", value=is_banned)
                embed.add_field(name="<:me:874509575716474880> About Me", value=desc)
                embed.add_field(name="👥 Friends Count", value=friend_count)
                embed.add_field(name="<:follower:874514734978854912> Followers Count", value=followers)
                embed.add_field(name="🕙 Created At", value=creation_date)
                embed.add_field(name="<:limited:874509891958607872> Limited Items", value=stuff)
                await ctx.reply(embed=embed, mention_author=False)
            except:
                await ctx.reply("<:wrong:773145931973525514> Oops! We have encountered an error. Please try again later :/")
                #await ctx.reply(e)
           



def setup(client):
    client.add_cog(GamesAPI(client))
