import asyncio
import re
from classes.application import Application, on_discord_message_received
from tests.support.mocks_factory import *

def test_radmin_message(mocker):
    app = Application(createBotClient(), "test-token")
    channel = createChannel(mocker.Mock())
    messages_to_test = ["!radmin", "!vpn", "!radminvpn"]
    author = createMember()
    for message in messages_to_test:
        channel.mock.reset()
        asyncio.run(on_discord_message_received(app, createMessage(message_content=message, message_channel=channel,message_author= author)))
        channel.mock.assert_called()        
        assert re.search('Juegos L\.P\.F', channel.mock.call_args_list[0][0][0], re.IGNORECASE) != None