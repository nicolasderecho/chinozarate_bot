import asyncio
import re
from classes.application import Application, on_discord_message_received
from tests.support.mocks_factory import *

def test_half_life_message(mocker):
    app = Application(createBotClient(), "test-token")
    channel = createChannel(mocker.Mock())
    messages_to_test = ["chino como juego al half life?",
                        "chino como juego al hl?",
                        "chino como juego al half-life?"]
    author = createMember()
    for message in messages_to_test:
        channel.mock.reset()
        asyncio.run(on_discord_message_received(app, createMessage(message_content=message, message_channel=channel,message_author= author)))
        channel.mock.assert_called()        
        assert re.search('youtube.com\/watch\?v=JoV9o6b91Sc', channel.mock.call_args_list[0][0][0], re.IGNORECASE) != None