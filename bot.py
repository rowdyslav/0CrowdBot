import os
# from webserver import keep_alive
import asyncio
import discord
from discord.ext import commands


# my_secret = os.environ['<secret_token>']
my_secret = 'MTA5NzkwOTcxNzE5NzY1NjA4NA.GUSA\
MZ.JB9_G2Fvwu5Es49_n_edOcwB2dmoTktTEgVKt4'

client = commands.Bot(command_prefix='0!', intents=discord.Intents.all())


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')
            print(f'Файл {filename[:-3]} загружен!')


async def main():
    async with client:
        await load()
        # keep_alive()
        await client.start(my_secret)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Работает в 0Crowd!'))
    print('Бот работает!')


asyncio.run(main())

# https://discord.com/api/oauth2/authorize?client_id=1097909717197656084&permissions=8&scope=bot
