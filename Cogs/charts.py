import discord
from discord.ext import commands
from PIL import Image
from io import BytesIO
from matplotlib import pyplot as plt

class Charts(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="hbchart")
    async def horizontal_bar_chart(self, ctx, *, args) -> plt.subplots():
        #print(args)
        args = tuple(args.split(' '))
        index = args.index('|')
        args = list(args)
        args.pop(index)
        args = tuple(args)
        before = args[:index]
        after = args[index:]
        plt.rcdefaults()
        fig, axes = plt.subplots()
        axes.barh(before, after, align='center')
        axes.set_xlabel("X Axis --->")
        axes.set_ylabel("Y Axis --->")
        axes.set_title("Horizontal Bar Chart")
        #plt.show()
        bufferobject = BytesIO()
        #plt.savefig(bufferobject, 'chart.png')
        with BytesIO() as img_bytes:
            plt.savefig(img_bytes, format='png')
            img_bytes.seek(0)
            read_image = bufferobject.read()
            await ctx.channel.send(
                    file=discord.File(fp=img_bytes, filename='qrcode.png')
                    )

def setup(client):
    client.add_cog(Charts(client))
