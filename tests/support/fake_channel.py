class FakeChannel():
    
    def __init__(self, mock):
        self.mock = mock
    
    async def send(self, *args):
        self.mock(*args)
        print("Fake channel received a command")
        
    async def purge(self, **kwargs):
        self.mock("purge")
        print("Fake purge called")