import asyncio
import re
from classes.application import Application, on_discord_message_received
from tests.support.mocks_factory import *

def test_counter_strike_server_message(mocker):
    app = Application(createBotClient(), "test-token")
    channel = createChannel(mocker.Mock())
    messages = ["!cs", "chino cuales eran los comandos del server del cs?",
                "chino cuales eran los comandos del server del counter?", 
                "chino cuales eran los comandos del server del counter-strike?", 
                "chino cuales eran los comandos del server del counter strike?", 
                "chino cuales eran los comandos del server del cstrike?", 
                "chino tirate los comandos del cs",
                "chino tirate los comandos del counter", 
                "chino tirate los comandos del counter-strike",
                "chino tirate los comandos del counter strike",
                "chino tirate los comandos del cstrike",
                "chino cuales son los comandos del server del counter?",
                "chino tira los comandos del cstrike",
                "chino tirame los comandos del cstrike",
                "chino tirá los comandos del cstrike",
                "chino tira los comandos de counter"]
    author = createMember()
    for message in messages:
        channel.mock.reset_mock()
        asyncio.run(on_discord_message_received(app, createMessage(message_content=message, message_channel=channel,message_author= author)))        
        message_response = channel.mock.call_args_list[0][0][0]
        assert re.search("bot_difficulty", message_response, re.IGNORECASE) is not None