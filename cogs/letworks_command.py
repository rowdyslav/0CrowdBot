import discord
from discord.ext import commands
from format_letwork import format_letwork


class LetWorksC(commands.Cog):
    def _init_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Команда testlw работает!')

    @commands.command()
    async def testlw(self, ctx, channel: discord.TextChannel, wday=0):
        content = format_letwork(wday)
        await channel.send(content) if channel else await ctx.send(content)


async def setup(client):
    await client.add_cog(LetWorksC(client))
