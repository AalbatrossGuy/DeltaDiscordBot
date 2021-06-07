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
        args = str(args).replace(' ', '')
        args = list(args)
        #print(args)
        tupbefore = []
        tupafter = []
        index = args.index('|')
        tupbefore = args[0:index]
        tupafter = args[index+1:]
        # print(tupbefore)
        # print(tupafter)
        plt.rcdefaults()
        fig, axes = plt.subplots()
        numbers = tupbefore
        labels = tupafter
        axes.barh(labels, numbers, align='center')
        axes.set_xlabel('X Axis --->')
        axes.set_ylabel("Y Axis --->")
        axes.set_title('Horizontal Bar Chart')
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
