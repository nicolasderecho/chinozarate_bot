class FakeChannel():
    
    def __init__(self, mock):
        self.mock = mock
        self.messages = [];
    
    async def send(self, *args):
        self.mock(*args)
        print("Fake channel received a command")
        
        
    async def history(self, **kwargs):
        self.mock("history");
        for i in range(len(self.messages)):
            yield self.messages[i]
        
    async def purge(self, **kwargs):
        self.mock("purge")
        print("Fake purge called")