from .silent_responder import SilentResponder

class SubclassTrackerMetaClass(type):
    subclasses = []
    ignored_classes = ["EventResponser"]
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        if name not in SubclassTrackerMetaClass.ignored_classes:
            SubclassTrackerMetaClass.subclasses.append(cls)
            print(f"Added {name} to the list")

class EventResponser(metaclass=SubclassTrackerMetaClass):

    def __init__(self, *, application, discord_message):
        self.application = application
        self.discord_message = discord_message
        self.event = discord_message.trigger
        self.message = discord_message.message
        self.channel = self.event.channel

    async def reply(self):
        raise "SUBCLASS"    
    
    @classmethod
    def can_handle(cls, discord_message):
        raise "SUBCLASS"
    
    @classmethod
    def responder_for(cls, discord_message, application):
        responder_class = next((subclass for subclass in cls.subclasses if subclass.can_handle(discord_message)), SilentResponder)
        return responder_class(discord_message=discord_message, application=discord_message)

