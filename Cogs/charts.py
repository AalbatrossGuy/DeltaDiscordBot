import discord
from discord.ext import commands
from PIL import Image
from io import BytesIO


class Charts(commands.Cog):
    def __init__(self, client):
        self.client = client





def setup(client):
    client.add_cog(Charts(client))
