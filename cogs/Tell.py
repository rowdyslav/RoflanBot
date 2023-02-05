import discord
from discord.ext import commands

class Tell(commands.Cog):
    def _init_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Команда tell работает!')

    @commands.command()
    async def tell(self, ctx, user: discord.User, *, mes):
        await user.send(f'{mes}')
        await ctx.message.delete()


async def setup(client):
    await client.add_cog(Tell(client))