import asyncio
import re
from classes.application import Application, on_discord_message_received
from tests.support.mocks_factory import *

def test_worms_message(mocker):
    app = Application(createBotClient(), "test-token")
    channel = createChannel(mocker.Mock())
    message = "!comandos"
    author = createMember()
    asyncio.run(on_discord_message_received(app, createMessage(message_content=message, message_channel=channel,message_author= author)))        
    message_response = channel.mock.call_args_list[0][0][0]
    assert re.search(r"!hangouts", message_response, re.IGNORECASE) is not None
    assert re.search(r"!diablolpf", message_response, re.IGNORECASE) is not None
    assert re.search(r"!juegoslpf", message_response, re.IGNORECASE) is not None
    assert re.search(r"!worms", message_response, re.IGNORECASE) is not None
    assert re.search(r"!cs", message_response, re.IGNORECASE) is not None