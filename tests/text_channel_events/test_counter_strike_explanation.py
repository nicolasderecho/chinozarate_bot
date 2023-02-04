import asyncio
import re
from classes.application import Application, on_discord_message_received
from tests.support.mocks_factory import *

def test_counter_strike_server_message(mocker):
    app = Application(createBotClient(), "test-token")
    channel = createChannel(mocker.Mock())
    messages = ["chino como configuro un server del cs?",
                "chino como configuro el server del cs?", 
                "chino como configuro un server del cstrike?", 
                "chino como configuro un server del counter?", 
                "chino como configuro un server del counter-strike?", 
                "chino como configuro un server del counter strike?"]
    author = createMember()
    for message in messages:
        channel.mock.reset_mock()
        asyncio.run(on_discord_message_received(app, createMessage(message_content=message, message_channel=channel,message_author= author)))        
        message_response = channel.mock.call_args_list[0][0][0]
        assert re.search("hay 2 formas", message_response, re.IGNORECASE) is not None