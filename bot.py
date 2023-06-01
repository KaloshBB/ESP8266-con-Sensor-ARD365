import discord
import time
from discord.ext import commands
import responses
import bot
import grafica



intents = discord.Intents.all()
bot = commands.Bot(command_prefix="#", intents=intents)

@bot.event
async def on_ready():
    print("online")
    channel = bot.get_channel(755235901046784051)
    await channel.send("online")

@bot.command(pass_context=True)
# async def perrito(ctx):

#     await ctx.send("PERRITOO", file=discord.File("YO pero con peluchito.png"))

async def nivelAgua(ctx):
    grafica.graficar()
    await ctx.send("Aqui tienes la grafica:", file=discord.File("nivelagua.png"))



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f"{username} said: '{user_message}' ({channel})")

    response = responses.handle_response(user_message)
    if response:
        await message.channel.send(response)

    await bot.process_commands(message)

def run_discord_bot():
    BOT_TOKEN = 'NTgzMDk0MTUwMjEyMDkxOTI1.GAgmeY.EirIkbJuI3rBHsJ3VA2RwNjKGENtEK0ImCGqkA'
    bot.run(BOT_TOKEN)

run_discord_bot()