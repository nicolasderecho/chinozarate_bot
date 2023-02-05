import re
from ...event_responder import EventResponser

class CleanMessagesHandler(EventResponser):
    async def reply(self):
        try:
            async for message in self.event.channel.history(limit=200):
                await message.delete()
        except Exception as e:
            print(f"Can't clean channel: {e}")

    @classmethod
    def can_handle(cls, discord_event):
        return re.search('chino limpia el canal', discord_event.message.content, re.IGNORECASE)