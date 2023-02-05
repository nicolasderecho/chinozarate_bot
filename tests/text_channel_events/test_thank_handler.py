import asyncio
from classes.application import Application, on_discord_message_received
from tests.support.mocks_factory import *

def test_thanks_handler(mocker):
    app = Application(createBotClient(), "test-token")
    channel = createChannel(mocker.Mock())
    messages_to_test = ["gracias chino"]
    author = createMember()
    possible_answers = [
          'De nada campeón! Vamos floresta!',
          f"De nada {author.mention}?",
          'De nada guachín',
          'Que sea la última vez que me rompés las pelotas!',
          'Chupame un huevo'
      ]
    for message in messages_to_test:
        channel.mock.reset()
        asyncio.run(on_discord_message_received(app, createMessage(message_content=message, message_channel=channel,message_author= author)))
        assert any([val[0][0] in possible_answers for val in channel.mock.call_args_list]), "The thanks message '{}' was not replied correctly".format(message)