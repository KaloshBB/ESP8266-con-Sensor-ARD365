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
    #esta linea solo existe para que el bot mande un mensaje cuando se prenda, no es necesaria. Ademas de que el canal al que se manda el mensaje debe ser cambiado por el canal de texto que se desee
    channel = bot.get_channel(iddelcanaldetexto)
    await channel.send("online")

@bot.command(pass_context=True)
# async def perrito(ctx):

#     await ctx.send("PERRITOO", file=discord.File("YO pero con peluchito.png"))

#ESTA ES LA FUNCION QUE SE ENCARGA DE MANDAR LA GRAFICA AL CANAL DE TEXTO, TENER CUIDADO CON LA RUTA DE LA GRAFICA, YA QUE EL BOT SOLO LEE LOS DATOS DE SU MISMA CARPETA DEL PROYECTO, ENTONCES SI LA GRAFICA ESTA EN OTRA CARPETA, NO LA VA A ENCONTRAR
async def nivelAgua(ctx):
    grafica.graficar()
    await ctx.send("Aqui tienes la grafica:", file=discord.File("nivelagua.png"))


    #Tan solo se encarga de mostrar en consola el mensaje que se mando en cualquier canal de texto al que puede accesar el bot, mostrando los datos del usuario que mando el mensaje, el mensaje que mando y el canal en el que lo mando.
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

    #este es el inicion de sesion del bot, se debe de cambiar el token por el token del bot que se desea usar. EL TOKEN SE SACA DE LA PAGINA: https://discord.com/developers/applications EN CASO DE SER NECESARIO VER UN TUTORIAL DE COMO CREAR EL BOT EN ESA PAGINA Y COMO OBTENER EL TOKEN
def run_discord_bot():
    BOT_TOKEN = 'insertar token aqui'
    bot.run(BOT_TOKEN)

run_discord_bot()