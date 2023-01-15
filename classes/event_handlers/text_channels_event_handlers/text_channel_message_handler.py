# def all_subclasses(cls):
#     return set(cls.__subclasses__()).union(
#         [s for c in cls.__subclasses__() for s in all_subclasses(c)])

# class PluginBase:
#     subclasses = []

#     def __init_subclass__(cls, **kwargs):
#         super().__init_subclass__(**kwargs)
#         cls.subclasses.append(cls)

# class Plugin1(PluginBase):
#     pass

# class Plugin2(PluginBase):
#     pass

class TextChannelMessageHandler():
    subclasses = []
    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)
    
    def __init__(self, *, application, discord_message):
        self.application = application
        self.discord_message = discord_message
    
    def reply(self):
        raise "Subclass"
    
    @classmethod
    def can_handle(discord_message):
        raise "Subclass"