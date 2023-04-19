from discord.ext import commands
# import discord
import datetime
import pytz
from random import choice


class LetWorksC(commands.Cog):
    def _init_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Команда testlw работает!')

    @commands.command()
    async def testlw(self, ctx, channel):
        now = datetime.datetime.now(
            pytz.timezone('Europe/Moscow'))
        print('команда робит')
        await channel.send(
            open('letworks.txt').read()
            ).replace('<date>', now.strftime("%d.%m.%Y").
                      replace('<cit>', choice(open('cits.txt'))))


async def setup(client):
    await client.add_cog(LetWorksC(client))
set()
