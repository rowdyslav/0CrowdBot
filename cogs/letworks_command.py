import discord
from discord.ext import commands
from datetime_funcs import format_letwork


class LetWorksC(commands.Cog):
    def _init_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Команда testlw работает!')

    @commands.command()
    async def testlw(self, ctx, channel: discord.TextChannel, wday=0):
        await channel.send(format_letwork(wday))


async def setup(client):
    await client.add_cog(LetWorksC(client))
