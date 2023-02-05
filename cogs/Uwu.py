import discord
from discord.ext import commands
from pathlib import Path
import random
import os

class Uwu(commands.Cog):
    def _init_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Команда uwu работает!')

    @commands.command(aliases=['uvu','uw','юву'])
    async def uwu(self, ctx):
        dir_path = Path('snds', 'uwus')
        await ctx.send('uwu', tts=True, file=discord.File(Path('snds', 'uwus', f'uwu{random.randint(1, len([entry for entry in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, entry))]))}.mp3')))


async def setup(client):
    await client.add_cog(Uwu(client))