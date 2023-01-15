
class FakeMessage():
    def __init__(self,*, author, channel, content, **kwargs):
        self.author = author
        self.channel = channel
        self.content = content
    
        