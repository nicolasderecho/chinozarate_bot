from .discord_message import DiscordMessage
from .event_responder import EventResponser
from .event_handlers.text_channels_event_handlers import *

async def on_discord_message_received(application, messageEvent):
    if messageEvent.author == application.client.user:
        return
    
    discord_message = DiscordMessage(application, messageEvent)    
    event_handler = EventResponser.responder_for(application=application, discord_message=discord_message)
    await event_handler.reply()

class Application():
    def __init__(self, client, token):
        self.client = client
        self.token = token
        self.addOnReadyListener()
        self.addOnMessageListener()
        
    def addOnReadyListener(self):
        @self.client.event
        async def on_ready():
            print(f'{self.client.user} has connected to Discord!')
    
    
    def addOnMessageListener(self):    
        @self.client.event
        async def on_message(message):
            await on_discord_message_received(self, message)
                
    def start(self):
        self.client.run(self.token)                