import re
from ...event_responder import EventResponser

class CounterStrikeCommandsHandler(EventResponser):
    async def reply(self):
        await self.channel.send(self.commands())
        
    def commands(self):
        return """```md
Comandos Usando Zbots

bot_add_t  => agrega un terro
bot_add_ct => agrega un counter
bot_kick   => raja a todos los bots de la partida
bot_kick NombreDelBot => solo raja a ese bot (Ej: bot_kick adam)

Comandos Usando PodBot

Se agregan bots usando pb add [skill [personality [team [model [name]]]]]
pb add 100 5 2 => Agrega un Counter con inteligencia 100 y personalidad(agresivo/defensivo) aleatoria
pb add 100 5 1 => Agrega un Terro con inteligencia 100 y personalidad(agresivo/defensivo) aleatoria
pb removebots => Raja a todos los bots
pb_bot_join_team T => fuerza que los bots sean Terro
pb_bot_join_team CT => fuerza que los bots sean Counter
pb help => te muestra los comandos que se pueden usar.

Comandos del Juego

sv_restart SEGUNDOS => restartea la partida en X segundos (Ej: sv_restart 10)
mp_autoteambalance 0 => deja de balancear automáticamente los equipos.
mp_limitteams 0 => deja de forzarte a que la cantidad de terrors y counters sea balanceada.
bot_difficulty Numero => setea la dificultad de los bots. Tiene que ser un número de 0 a 3 (Ej: bot_difficulty 3 hace que todos los bots estén en la dificultad más difícil. con 0 sería la más fácil).
changelevel MAPA => cambia automáticamente al mapa especificado (Ej: changelevel de_dust te manda al mapa de_dust)
users   => Lista los usuarios conectados junto con sus datos (Ej: ID)
kick USER_ID  => kickea al usuario especificado (tenés que poner el ID o el nombre)
sv_restart SEGUNDOS   => restartea la partida en X segundos especificados.
mp_winlimit NUMERO    => Actualiza el valor de victorias que el equipo debe conseguir para ganar.
mp_roundlimit NUMERO  => Actualiza la cantiad de rondas a jugar hasta que se cambie el mapa.
mp_buytime NUMERO     => Determina cuanto tiempo tenés para comprar armas. El numero está expresado en minutos. EJ: 1.25

Fuente => http://cs1-6cfg.blogspot.com/p/cs-16-client-and-console-commands.html
```"""
      
        
    @classmethod
    def can_handle(cls, discord_event):
        return  re.search('!cs', discord_event.message.content, re.IGNORECASE) or \
                re.search('chino cuales (eran|son) los comandos (del server)? (de|del) (cs|cstrike|counter-strike|counter)\??', discord_event.message.content, re.IGNORECASE) or \
                re.search('chino (tirate|tir(a|á)|tirame) los comandos (de|del) (cs|cstrike|counter-strike|counter)', discord_event.message.content, re.IGNORECASE)