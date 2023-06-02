import discord
import time
from discord.ext import commands
import bot

#Este archivo se encarga de manejar las respuestas del bot de discord, segun el mensaje que reciba el bot, este respondera con un mensaje diferente. NO SE COMO FUNCIONA BIEN XDDDDDD

def handle_response(message):
    p_message = message.lower()
    prefix = '#'
    if p_message.startswith(prefix):
        if p_message == (prefix + 'jijijija'):
            return ':JijijijaR:'
        if p_message == (prefix + 'perrito'):
            return ''


    return None
        