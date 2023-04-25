# import discord
from discord.ext import commands
from datetime_funcs import format_letwork, seconds_left
import asyncio


class LetWorksM(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.channel_id = 1081624019842908252

    @commands.Cog.listener()
    async def on_ready(self):
        print('Сообщения LetWorks работают!')
        await self.letworks_task()

    async def letworks_task(self):
        while True:
            print('Летворк таск сработал, сейчас будет ожидание')
            await asyncio.sleep(seconds_left())
            print('Ожидание закончено! Сообщение должно было отправиться')
            channel = self.client.get_channel(self.channel_id)
            content = format_letwork()
            await channel.send(content)
            await asyncio.sleep(1)


async def setup(client):
    await client.add_cog(LetWorksM(client))
