#NOTES: ADD A SPACE INFRONT OF EACH COMMAND
import discord
import os
import random
from discord.ext import commands
import time
import datetime
from datetime import datetime
from replit import db
from keep_alive import keep_alive
import pymongo
import dns
import discord.utils
from discord.utils import get
from pymongo import MongoClient
import math
import collections
from collections import Counter
#from commands import update_log
from functions import *
import config


prefix = '.bread'
madlibs = {}
collectors = []
pantry_limit = config.pantry_limit
common_bread = config.common_bread
rare_bread = config.rare_bread
mythical_bread = config.mythical_bread
legendary_bread = config.legendary_bread
updateLog = config.updateLog
helpContent = config.helpContent
faqContent = config.faqContent



      









#database stuff
cluster = pymongo.MongoClient(os.getenv('CONNECTION_URL'))
database = cluster["UserData"]
collection = database["UserData"]














client = commands.Bot(command_prefix='.bread ')




  






@client.event
async def on_ready():
    
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('bot is being rewritten'))
    prefix = '.bread'

@client.event
async def on_guild_join(guild):
    
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('.bread help; In '+str(len(client.guilds))+' servers'))
    prefix = '.bread'


client.load_extension("cogs.misc")
client.load_extension("cogs.game") 




keep_alive()

client.run(os.getenv('TOKEN'))
