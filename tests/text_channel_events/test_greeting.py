import asyncio
from classes.application import Application, on_discord_message_received
from tests.support.mocks_factory import *

def test_greetings(mocker):
    #assert discord_channel.send.call_count == 0
    app = Application(createBotClient(), "test-token")
    channel = createChannel(mocker.Mock())
    messages_to_test = ["Hola chino", "como va chino?"]
    author = createMember()
    possible_answers = [
          'Aloja!! Aguante Allboys!!!',
          '¿Qué acelga?',
          '¿Todo bien?',
          '¿Todo tranca?',
          f"¿Como va {author.mention}?"
      ]
    for message in messages_to_test:
        channel.mock.reset()
        asyncio.run(on_discord_message_received(app, createMessage(message_content=message, message_channel=channel,message_author= author)))
        #channel.mock.reply.assert_called_with("Hello!")
        assert any([val[0][0] in possible_answers for val in channel.mock.call_args_list]), "The greeting message '{}' was not replied correctly".format(message)