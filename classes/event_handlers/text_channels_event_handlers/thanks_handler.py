import re
import random
from ...event_responder import EventResponser

class ThankHandler(EventResponser):
    async def reply(self):
        await self.channel.send(random.choice(self.possible_answers()))
        
    def possible_answers(self):
      return [
          'De nada campeón! Vamos floresta!',
          f"De nada {self.event.author.mention}?",
          'De nada guachín',
          'Que sea la última vez que me rompés las pelotas!',
          'Chupame un huevo'
      ]
        
        
    @classmethod
    def can_handle(cls, discord_event):
        return re.search('gracias chino', discord_event.message.content, re.IGNORECASE)