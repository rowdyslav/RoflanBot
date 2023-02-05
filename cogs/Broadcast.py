import discord
from discord.ext import commands

class Broadcast(commands.Cog):
    def _init_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Команда broadcast работает!')

    @commands.command(aliases=['bc'])
    @commands.has_permissions(mention_everyone = True)
    async def broadcast(self, ctx, *, mes):
        await ctx.message.delete()
        await ctx.send(f'@everyone, {mes}')


async def setup(client):
    await client.add_cog(Broadcast(client))