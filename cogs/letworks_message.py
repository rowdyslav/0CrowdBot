# import discord
from discord.ext import commands, tasks
from datetime_funcs import format_letwork, seconds_left
import asyncio


class LetWorksM(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.channel_id = 1081624019842908252
        self.letworks_task.start()

    @commands.Cog.listener()
    async def on_ready(self):
        print('Сообщения LetWorks работают!')

    def cog_unload(self):
        self.letworks_task.cancel()

    @tasks.loop(seconds=1)
    async def letworks_task(self):
        print('летворк таск сработал ща ждать будет')
        await asyncio.sleep(seconds_left())
        channel = self.client.get_channel(self.channel_id)
        content = format_letwork()
        await channel.send(content)

    @letworks_task.before_loop
    async def before_letworks_task(self):
        await self.client.wait_until_ready()
        print('Ожидание закончено! Сообщение должно было отправиться')


async def setup(client):
    await client.add_cog(LetWorksM(client))
