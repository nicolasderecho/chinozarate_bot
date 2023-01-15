class FakeChannel():
    
    def __init__(self, mock):
        self.mock = mock
    
    async def send(self, *args):
        self.mock(*args)
        print("Fake channel received a command")