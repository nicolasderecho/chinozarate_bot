import re
from ...event_responder import EventResponser

class HalfLifeLpfHandler(EventResponser):
    async def reply(self):
        await self.channel.send("https://www.youtube.com/watch?v=JoV9o6b91Sc")
        
    @classmethod
    def can_handle(cls, discord_event):
        return re.search('como (juego|gano) (a|al|el)? (half-life|hl|half life)\?', discord_event.message.content, re.IGNORECASE)