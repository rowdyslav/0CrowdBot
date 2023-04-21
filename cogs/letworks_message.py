# import discord
from discord.ext import commands, tasks
from format_letwork import format_letwork
import asyncio
from datetime import datetime as dt
from pytz import timezone


# Создание класса Cog
class LetWorksM(commands.Cog):
    def _init_(self, client):
        self.client = client
        self.channel_id = 1092784583008854026
        self.message_time = "7:00"
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
            now = dt.now(
                timezone('Europe/Moscow'))
            if now.strftime("%H:%M") == self.message_time:
                channel = self.client.get_channel(self.channel_id)
                content = format_letwork()
                await channel.send(content)
                await asyncio.sleep(60)

    @letworks_task.before_loop
    async def before_letworks_task(self):
        await self.client.wait_until_ready()


async def setup(client):
    await client.add_cog(LetWorksM(client))
