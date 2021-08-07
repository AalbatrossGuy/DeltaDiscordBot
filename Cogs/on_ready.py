# Coding=UTF8
# !python
# !/usr/bin/env python3

import os
import subprocess

from discord import Activity
from discord.ext import commands


def version_info():
    version = 'No Data'
    date = 'No Data'
    gitlog = subprocess.check_output(
        ['git', 'log', '-n', '1', '--date=iso']).decode()
    for line in gitlog.split('\n'):
        if line.startswith('commit'):
            version = line.split(' ')[1]
        elif line.startswith('Date'):
            date = line[5:].strip()
            date = date.replace(' +', '+').replace(' ', 'T')
        else:
            pass
    return version, date


class OnReady(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        version = version_info()[0][:7]

        print("Bot up and running!")
        cogs = [x[:-3] for x in os.listdir('./Cogs')]
        for cogsname in cogs:
            if cogsname == "__pycach":
                continue
            else:
                try:
                    print(f"Loaded cogs.{cogsname} successfully!")
                    await self.client.change_presence(activity=Activity(name=f"branch {version}", type=2))
                except:
                    pass


def setup(client):
    client.add_cog(OnReady(client))
