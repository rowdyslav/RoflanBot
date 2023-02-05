import discord
from discord.ext import commands
import os
import asyncio
from pathlib import Path

client = commands.Bot(command_prefix='rdy.', intents=discord.Intents.all())

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')
            print(f'Файл {filename[:-3]} загружен!')

async def main():
    async with client:
        await load()
        with open(Path('token.txt'), 'r', encoding='utf-8') as token:
            await client.start(token.read())

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('геншин импакттт'))
    print('бот робит двк')

@client.event
async def on_message(message):
    if message.guild is None:
        logchannel = client.get_channel(1070014822034444300)
        await logchannel.send(f'{message.author} - {message.content}')
    await client.process_commands(message)

@client.event
async def on_command(ctx):
    logchannel = client.get_channel(1070014822034444300)
    await logchannel.send(f'{ctx.message.author} -> {ctx.message.content}')

asyncio.run(main())

#https://discord.com/api/oauth2/authorize?client_id=1068555747664871465&permissions=8&scope=bot