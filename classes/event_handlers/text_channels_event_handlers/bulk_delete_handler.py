import re
from ...event_responder import EventResponser
from functools import reduce

class CommandsHandler(EventResponser):
    async def reply(self):
        try:
            await self.event.channel.purge(limit=100)
        except Exception as e:
            print(f"Can't prune channel: {e}")

    @classmethod
    def can_handle(cls, discord_event):
        return re.search('chino borra los mensajes', discord_event.message.content, re.IGNORECASE) or re.search('chino borra todos los mensajes', discord_event.message.content, re.IGNORECASE)