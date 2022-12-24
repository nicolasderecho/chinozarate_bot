# bot.py
import os

import discord
from dotenv import load_dotenv
from classes.application import Application 

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

client = discord.Client(intents=discord.Intents.all())

app = Application(client, TOKEN)

app.start()

# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')


# @client.event
# async def on_message(message):
#     print(f"Message Received {message.content}")
#     if message.author == client.user:
#         print("Rajandingong")
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')
        

#client.run(TOKEN)
