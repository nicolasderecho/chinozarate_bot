import os

import discord
from dotenv import load_dotenv
import sys
root = os.path.dirname(os.path.realpath('__file__'))
sys.path.insert(0, root)

from classes.application import Application 

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

client = discord.Client(intents=discord.Intents.all())

app = Application(client, TOKEN)

app.start()