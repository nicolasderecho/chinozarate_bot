import asyncio
from classes.application import Application, on_discord_message_received
from tests.support.mocks_factory import *

def test_clean_message(mocker):
    app = Application(createBotClient(), "test-token")
    channel = createChannel(mocker.Mock())
    messages = ["chino limpia el canal"]
    author = createMember()
    for message in messages:
        channel.mock.reset()
        asyncio.run(on_discord_message_received(app, createMessage(message_content=message, message_channel=channel,message_author= author)))        
        channel.mock.assert_called_with("history")