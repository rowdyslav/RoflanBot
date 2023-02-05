import discord
from discord.ext import commands
import random

class Ping(commands.Cog):
    def _init_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Команда ping работает!')

    @commands.command(aliases=['pong'])
    async def ping(self, ctx):
        await ctx.send(f'pong ebat {random.randint(1, 656)}')


async def setup(client):
    await client.add_cog(Ping(client))