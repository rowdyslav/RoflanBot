import discord
from discord.ext import commands

class Say(commands.Cog):
    def _init_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Команда say работает!')

    @commands.command()
    async def say(self, ctx, *, mes):
        await ctx.message.delete()
        await ctx.send(f'{mes}')


async def setup(client):
    await client.add_cog(Say(client))