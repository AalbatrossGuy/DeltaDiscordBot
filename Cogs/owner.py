import discord
from discord.ext import commands

# Owner ONLY commands

class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client 






def setup(client):
    client.add_cog(Owner(client))
