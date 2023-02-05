import discord
from discord.ext import commands

class Bio(commands.Cog):
    def _init_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Команда bio работает!')

    @commands.command(aliases=['biography'])
    async def bio(self, ctx):
        await ctx.send('Меня зовут сережа (прозвище пират), моя любимая фраза: "йо-хо-хо и бутылка лева"')


async def setup(client):
    await client.add_cog(Bio(client))