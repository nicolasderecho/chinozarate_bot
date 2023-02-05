import asyncio
import re
from classes.application import Application, on_discord_message_received
from tests.support.mocks_factory import *

def test_google_drive_lpf_message(mocker):
    app = Application(createBotClient(), "test-token")
    channel = createChannel(mocker.Mock())
    messages_to_test = ["!carpetalpf", 
                        "chino cual es la carpeta de lpf?",
                        "chino tirame la carpeta de lpf",
                        "chino tirate la carpeta de lpf",
                        "chino tira la carpeta de lpf",
                        "chino tirá la carpeta de lpf"]
    author = createMember()
    for message in messages_to_test:
        channel.mock.reset()
        asyncio.run(on_discord_message_received(app, createMessage(message_content=message, message_channel=channel,message_author= author)))
        channel.mock.assert_called()        
        assert re.search('https://drive.google.com/drive/folders/1yY2T2Ej2BP7TcgbZVWEFAR0v48IEMm34', channel.mock.call_args_list[0][0][0], re.IGNORECASE) != None