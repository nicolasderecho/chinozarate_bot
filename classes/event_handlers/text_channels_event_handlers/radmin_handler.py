import re
from ...event_responder import EventResponser

class RadminLpfHandler(EventResponser):
    async def reply(self):
        await self.channel.send(self.radmin())
        
        
    def radmin(self):
        return """```md
Red: Juegos L.P.F
Password: juegosLPF2019!
```"""
        
    @classmethod
    def can_handle(cls, discord_event):
        return  re.search('!radmin', discord_event.message.content, re.IGNORECASE) or \
                re.search('!radminlpf', discord_event.message.content, re.IGNORECASE) or \
                re.search('!vpn', discord_event.message.content, re.IGNORECASE)