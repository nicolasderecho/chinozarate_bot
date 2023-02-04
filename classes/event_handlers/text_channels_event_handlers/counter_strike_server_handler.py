import re
from ...event_responder import EventResponser

class CounterStrikeCommandsHandler(EventResponser):
    async def reply(self):
        await self.channel.send(self.large_command())
            
    def large_command(self):
        return """Hay 2 formas. La primera es ingresando los comandos en la consola del server: https://ibb.co/J2bWGNG \n\nEs la más fácil aunque tiene la paja de que tenes que minimizar el juego un toque para meter los comandos.\n
La segunda implica bajar la consola del juego mientras estamos jugando y tirar los comandos desde ahí. Para eso primero que nada tenemos que mirar cual es la contraseña de RCON del server: https://ibb.co/dDc6J4K\n
Una vez que sabemos esa contraseña lo que hacemos es conectarnos al server normalmente, abrimos la consola del juego y tipeamos lo siguiente:
        ```md
rcon_password PASSWORD```
Una vez hecho esto ya podemos tirar los comandos desde la consola del juego poniendo el prefijo rcon antes de cada comando.\nPor Ejemplo si el password de RCON fuera 'lpf':
        ```rcon_password lpf
rcon mp_autoteambalance 0
rcon bot_add_t
rcon sv_restart 10```
Bue y así con cualquier comando que quisieras tirar.\nOjo con poner mal el password de RCON porque podés quedar banneado. Eso le pasó a Nicolás una vez.
"""


    @classmethod
    def can_handle(cls, discord_event):
        return  re.search('chino como configuro (un|el) server (de|del) (cs|cstrike|counter-strike|counter|counter strike)\??', discord_event.message.content, re.IGNORECASE) 