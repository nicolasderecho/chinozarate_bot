import re
import random
from ...event_responder import EventResponser

class GreetingHandler(EventResponser):
    
    def possible_answers(self):
       return [
          'Aloja!! Aguante Allboys!!!',
          '¿Qué acelga?',
          '¿Todo bien?',
          '¿Todo tranca?',
          f"¿Como va {self.event.author.mention}?"
        ]
    
    async def reply(self):
        await self.channel.send(random.choice(self.possible_answers()))
        
    @classmethod
    def can_handle(cls, discord_event):
        return re.search("hola chino", discord_event.message.content, re.IGNORECASE) or re.search("como va chino?", discord_event.message.content, re.IGNORECASE)