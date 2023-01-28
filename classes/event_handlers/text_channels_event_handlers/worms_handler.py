import re
from ...event_responder import EventResponser

class WormsHandler(EventResponser):
    async def reply(self):
        await self.channel.send(self.worms_text())
        
        
    def worms_text(self):
        return """```md
Sacado de la sección [Chat command interface de esta página](https://worms2d.info/RubberWorm)

/help	Muestra la lista de comandos
/show	Muestra la lista de features habilitados
/showme	Lo mismo que show pero solo lo muestra al que crea la partida
/clear	Deshabilita todos los features.
/sdet o /multishot	Disparar no termina el turno.
/ldet o /stoicworm	Perder el control no finaliza el turno
/fdpt o /nopause	El timer no se pausa mientras disparás
/ir o /rope+	Habilita la cuerda mejorada.
/rubber### [0–255]	Habilita el feature bouncing worms(0 es nada y 255 es full)
/version### [1–255]	Habilita el feature arbitrary version override.
/version o /fr o /ts3	Habilita el feature teststuff3
/antisink	Los worms no se hunden
/visc### [0–255]	Establece la viscosidad del aire. Número impar afecta a los worms tambien.
/wind### [0–255]	Establece la respuesta del viento. Número impar afecta a los worms tambien.
1 a 255 ... Baja sensibilidad al viento
255 ... misma sensibilidad al viento que la bazooka

/jetpack### [1–255]	Establece el combustible del jetpack.
Sin ningún valor ... Combustible infinito

/friction### [1–100]	Establece la fricción del terreno
1 a 95 ....... alta fricción
96 .......... fricción por defecto
97 a 99 ...... baja fricción
100 .......... sin fricción
más de 100 .. anti-friccion

/glue	Lo mismo que friction1
/ice	Lo mismo que friction99
/gravity### [−64 a 63]	Establece la fuerza de la gravedad.
/pbh### [−32 a 31]	Black Hole proporcional (la variable es gravitational strength)
/cbh### [−32 a 31]	Black hole constante (la variable es gravitational strength)
/defg	Deshabilita todas las modificaciones hechas sobre la gravedad
/cratelimit### [1–255]	Establece el número máximo de cajas que pueden co-existir
/craterate### [1–255]	Establece el número de cajas que aparecen por turno y habilita el contador de cajas (crate counter)
/cratecount	Lo mismo que /craterate1 (Solo habilita el contador de cajas).
/crateshower Habilita la lluvia continua de cajas.
      ```"""
        
    @classmethod
    def can_handle(cls, discord_event):
        return re.search('!worms', discord_event.message.content, re.IGNORECASE) or re.search("chino tirate los comandos del worms", discord_event.message.content, re.IGNORECASE) or re.search("chino tirá los comandos del worms", discord_event.message.content, re.IGNORECASE) or re.search("chino tira los comandos del worms", discord_event.message.content, re.IGNORECASE)