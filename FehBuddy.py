# FehBuddy.py
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#GUID = os.getenv('DISCORD_GUILD')

#client = discord.Client()
bot = commands.Bot(command_prefix='FEH')


@bot.event
async def on_ready():
    #guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    #print(
        #f'{bot.user.name} is connected to the following guild:\n'
        #f'{bot.guilds[0].name}(id: {bot.guilds[0].id})'
    #)
    
    guilds = '\n - '.join([guild.name + " ID: " + str(guild.id) for guild in bot.guilds])
    print(f'{bot.user.name} is connected to the following guilds:\n - {guilds}')
    members = '\n - '.join([member.name for member in bot.guilds[1].members])
    print(f'Guild Members:\n - {members}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == ('FEH' or 'feh' or 'Feh'):        
        response = 'Dear ' + '<@'+str(message.author.id)+'>' + ' Fire Emblem Heroes is the best Mobile Gacha Game ever created by lord Kaga sent from the heavens'
        await message.channel.send(response)


bot.run(TOKEN)
