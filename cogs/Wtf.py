import discord
from discord.ext import commands
import random
from pathlib import Path

class Wtf(commands.Cog):
    def _init_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Команда wtf работает!')

    @commands.command()
    async def wtf(self, ctx):
        with open(Path('txs','wtf.txt'), 'r', encoding='utf-8') as otvs:
            await ctx.send(random.choice(otvs.readlines()))


async def setup(client):
    await client.add_cog(Wtf(client))