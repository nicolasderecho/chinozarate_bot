import re
from ...event_responder import EventResponser

class GoogleDriveLpfHandler(EventResponser):
    async def reply(self):
        await self.channel.send("https://drive.google.com/drive/folders/1yY2T2Ej2BP7TcgbZVWEFAR0v48IEMm34")
        
    @classmethod
    def can_handle(cls, discord_event):
        return  re.search('!carpetalpf', discord_event.message.content, re.IGNORECASE) or \
                re.search('chino (tira|tirá|tirame|tirate|cual es) la carpeta de lpf\/??', discord_event.message.content, re.IGNORECASE)