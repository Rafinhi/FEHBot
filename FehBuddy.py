# FehBuddy.py
import os

import discord
import random
import io
import aiohttp
from dotenv import load_dotenv
from discord.ext import commands
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#GUID = os.getenv('DISCORD_GUILD')

driver = browser = webdriver.Chrome(executable_path=r"C:\chromedriver.exe") #chromedriver does not have to be in PATH anymore

#client = discord.Client()
intents = discord.Intents.default()
intents.typing = False
intents.presences = True
intents.members = True
bot = commands.Bot(command_prefix='`' , intents=intents)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='Thracia 776'))

    #guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    #print(
        #f'{bot.user.name} is connected to the following guild:\n'
        #f'{bot.guilds[0].name}(id: {bot.guilds[0].id})'
    #)
    
    guilds = '\n - '.join([guild.name + " ID: " + str(guild.id) for guild in bot.guilds])
    print(f'{bot.user.name} is connected to the following guilds:\n - {guilds}')
    members = '\n - '.join([member.name for member in bot.guilds[1].members])
    print(bot.guilds[1].name + f' Guild Members:\n - {members}')
    # Append-adds at last 
    #file1 = open("myfile.txt","a")#append mode 
    #file1.write(members) 
    #file1.close() 



@bot.command(name='quote', help='Random quote from Fire Emblem Series')
async def feh_quote(ctx):
    feh_quotes = [
        'She\'s my booty! I\'m takin\' her back to be my wife. She\'s a keeper, wouldn\'t ya say?',
        'You\'re strong, reliable, ... and slow! You\'re the one, hands down! Hahahaa',
        (
            'Alvis... YOU BASTARD!!!'
        ),
        ('OK, let\'s see... Saint Elmine, praise be your graces. Please ensure that no one dies in this battle.'
         'Please grant me speed to heal my allies\' wounds. And, um, what else... I want Hector to give me a lot of gold,'
         ' and I want to get all the good food and only ever have to do the fun jobs,'
         ' and I want a servant who does whatever I say, and everyone should worship me and give me things, and...uhh...'
         )
    ]

    response = random.choice(feh_quotes)
    await ctx.send(response)

@bot.command(name='Edelgard', help='Praises lady Edelgard')
async def edelgard(ctx):
        response = 'Lady Edelgard is the most beautiful female in existence'
        await ctx.send(response)

@bot.command(name='random_hero', help='Generates link to random heroes from given range.')
async def roll(ctx, number_of_heroes: int, highest_id: int):
    #roll = [
     #   str(random.choice(range(1, highest_id + 1)))
      #  for _ in range(number_of_heroes)
    #]
    #await ctx.send(', '.join(roll))
    await ctx.send('Your random hero is: Claude: Almyra\'s King')

@bot.command(name='stats', help='Displays stats of chosen hero')
async def stats(ctx, name_of_hero: str):
    heroes=[] #list of heroes
    driver.get("https://feheroes.gamepedia.com/List_of_Heroes")
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    for a in soup.findAll('a', href= True):
        name=a.find('title')
        heroes.append(a.text)
    

    df = pd.DataFrame({'Hero Name':heroes}) #data frames are cool
    df.to_csv('heroes.csv', index=False, encoding='utf-8')
    
    await ctx.send('Your hero stats are: ')

    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if (message.content == "FEH" or message.content == "feh" or message.content == "Feh"): #triggers only if whole message consists of only this word 
    #if "FEH" or "Feh" or "feh" in message.content: #triggers if message contains those words at all, i suggest not using it as it will trigger too often in casual conversations
        response = 'Dear ' + '<@'+str(message.author.id)+'>' + ' Fire Emblem Heroes is the best Mobile Gacha Game ever created by lord Kaga sent from the heavens' #tag user
        await message.channel.send(response)
        await message.author.send('👋') #send emoji to the user
        await message.author.send(file=discord.File('E:\Desktop\Memy\83351143_3145654125485916_4612996795201486848_n.jpg')) #send local image as private message
        emoji = '\N{THUMBS UP SIGN}' # or '\U0001f44d' or '👍'
        await message.add_reaction(emoji) #tag message with emoji
    await bot.process_commands(message) #as "on_message" overwrites the default processing we need to call it back by "await bot.process_commands(message)"

# @bot.command(name='Music', help='Plays best song') #one day bot will be able to play fire emblem theme song, but not today



bot.run(TOKEN)
