import discord
from discord.ext import commands
import aiohttp

intents = discord.Intents.default()  # Use default intents for now

client = commands.Bot(command_prefix='!', intents=intents)

@client.command()
async def animegirl(ctx):
    """Tìm kiếm ảnh gái anime ngẫu nhiên."""
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.waifu.im/random') as resp:
            data = await resp.json()
            image_url = data['url']

    await ctx.send(image_url)

# Replace with your bot token
client.run('YOUR_BOT_TOKEN')
