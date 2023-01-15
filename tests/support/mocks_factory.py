from .fake_client import FakeClient
from .fake_member import FakeMember
from .fake_user import FakeUser
from .fake_message import FakeMessage
from .fake_channel import FakeChannel

def createChannel(mock):
    return FakeChannel(mock)

def createBotClient(bot_user = None):
    return FakeClient(bot_user or FakeUser(10, "Test Bot", True))

def createUser(*, name, id, **kwargs):
    return FakeUser(id, name, kwargs)

def createMember(*, name="Fake User", id=11, **kwargs):
    return FakeMember(id=id,name=name, **kwargs)

def createMessage(*,message_content,message_channel, message_author=None):
    return FakeMessage(author= message_author or createMember(), channel=message_channel, content=message_content)