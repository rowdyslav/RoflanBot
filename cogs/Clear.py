import discord
from discord.ext import commands

class Clear(commands.Cog):
    def _init_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Команда clear работает!')

    @commands.command(aliases=['clr','клир','вынестимусор'])
    async def clear(self, ctx, mess_c: int):
        await ctx.channel.purge(limit=mess_c)


async def setup(client):
    await client.add_cog(Clear(client))