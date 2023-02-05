import re
from ...event_responder import EventResponser

class HangoutLpfHandler(EventResponser):
    async def reply(self):
        await self.channel.send("https://hangouts.google.com/call/2-gwIV3lJORWae0o9UuqAAEE")
        
    @classmethod
    def can_handle(cls, discord_event):
        return  re.search('!hangouts', discord_event.message.content, re.IGNORECASE) or \
                re.search('!hg', discord_event.message.content, re.IGNORECASE) or \
                re.search('chino (tirate|tira|tirá|armate) un (hangout|hg)', discord_event.message.content, re.IGNORECASE) or \
                re.search('chino (tirate|tira|tirá|armate) (hangout|hg)', discord_event.message.content, re.IGNORECASE)