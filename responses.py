import discord
import time
from discord.ext import commands
import bot

def handle_response(message):
    p_message = message.lower()
    prefix = '#'
    if p_message.startswith(prefix):
        if p_message == (prefix + 'jijijija'):
            return ':JijijijaR:'
        if p_message == (prefix + 'perrito'):
            return ''


    return None
        
