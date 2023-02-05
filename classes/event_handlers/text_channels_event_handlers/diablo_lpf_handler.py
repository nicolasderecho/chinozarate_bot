import re
from ...event_responder import EventResponser

class DiabloLpfHandler(EventResponser):
    async def reply(self):
        await self.channel.send("https://diablolpf.vercel.app/")
        
    @classmethod
    def can_handle(cls, discord_event):
        return re.search('!diablolpf', discord_event.message.content, re.IGNORECASE)