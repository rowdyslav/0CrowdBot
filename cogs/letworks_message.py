# import discord
from discord.ext import commands, tasks
import asyncio
import datetime
import pytz
from random import choice


# Создание класса Cog
class LetWorksM(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.channel_id = 1092784583008854026
        self.message_time = "13:58"
        self.letworks_task.start()

    @commands.Cog.listener()
    async def on_ready(self):
        print('Сообщения LetWorks работают!')

    def cog_unload(self):
        self.letworks_task.cancel()

    @tasks.loop()
    async def letworks_task(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            now = datetime.datetime.now(
                pytz.timezone('Europe/Moscow'))
            if now.strftime("%H:%M") == self.message_time:
                channel = self.client.get_channel(self.channel_id)
                await channel.send(
                        open('letworks.txt').read()
                        ).replace('<date>', now.strftime("%d.%m.%Y")
                                  .replace('<cit>', choice(open('cits.txt'))))
                await asyncio.sleep(60)

    @letworks_task.before_loop
    async def before_letworks_task(self):
        await self.client.wait_until_ready()


async def setup(client):
    await client.add_cog(LetWorksM(client))
