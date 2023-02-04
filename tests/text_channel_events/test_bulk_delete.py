import asyncio
from classes.application import Application, on_discord_message_received
from tests.support.mocks_factory import *

def test_worms_message(mocker):
    app = Application(createBotClient(), "test-token")
    channel = createChannel(mocker.Mock())
    messages = ["chino borra los mensajes", "chino borra todos los mensajes"]
    author = createMember()
    for message in messages:
        channel.mock.reset()
        asyncio.run(on_discord_message_received(app, createMessage(message_content=message, message_channel=channel,message_author= author)))        
        channel.mock.assert_called_with("purge")