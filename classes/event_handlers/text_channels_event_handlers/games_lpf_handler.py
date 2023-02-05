import re
from ...event_responder import EventResponser

class GamesLpfHandler(EventResponser):
    async def reply(self):
        await self.channel.send("https://mega.nz/#F!or41ESyb!H7_bZCtA4ubFm8qygjJk5Q")
        
    @classmethod
    def can_handle(cls, discord_event):
        return re.search('!juegoslpf', discord_event.message.content, re.IGNORECASE)