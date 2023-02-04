import re
from ...event_responder import EventResponser
from functools import reduce

class CommandsHandler(EventResponser):
    async def reply(self):
        await self.channel.send(reduce(lambda text, entry: text + f"!{entry[0]}: {entry[1]}\n\n", self.commands().items(), ""))
        
        
    def commands(self):
      return {
        'cs':        'te tira comandos para configurar un server del Counter Strike 1.6',
        'diablolpf': 'te tira la mejor pagina del diablo II del mundo entero, lejos pibe',
        'hangouts': 'te comparte un link de hangouts para unirse a una videollamada',
        'juegoslpf': 'te tira la pagina de Mega donde estan guardados todos los juegos',
        'worms': 'te tira comandos útiles cuando intentas levantar una partida del worms'
      }
        
    @classmethod
    def can_handle(cls, discord_event):
        return re.search('!comandos', discord_event.message.content, re.IGNORECASE)