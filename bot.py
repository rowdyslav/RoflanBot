import os
from webserver import keep_alive
import asyncio
import discord
from discord.ext import commands


token = os.environ['RoflanBot']

client = commands.Bot(command_prefix='rdy.', intents=discord.Intents.all())

rowdy = client.get_user(422102971904425984)
logchannel = client.get_channel(1070014822034444300)


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')
            print(f'Файл {filename[:-3]} загружен!')


async def main():
    async with client:
        await load()
        keep_alive()
        await client.start(token)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('геншин импакттт'))
    print('бот робит двк')


@client.event
async def on_message(message):
    if message.guild is None:
        await rowdy.send(f'{message.author} - {message.content}')
    await client.process_commands(message)


@client.event
async def on_command(ctx):
    await logchannel.send(f'{ctx.message.author} -> {ctx.message.content}')

asyncio.run(main())

# https://discord.com/api/oauth2/authorize?client_id=1068555747664871465&permissions=8&scope=bot
