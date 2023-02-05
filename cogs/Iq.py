import discord
from discord.ext import commands
import random
from pathlib import Path

class Iq(commands.Cog):
    def _init_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Команда iq работает!')

    @commands.command(aliases=['ум','умом','айку'])
    async def iq(self, ctx):
        with open(Path('txs','umni.txt'), 'r', encoding='utf-8') as umni:
            if str(ctx.message.author.id) not in umni.readlines()[0].split():
                await ctx.send(f'{random.randint(1, 228)}')
            else:
                await ctx.send(f'{random.randint(345, 350)}')


async def setup(client):
    await client.add_cog(Iq(client))