class Application():
    def __init__(self, client, token):
        self.client = client
        self.token = token
        self.addOnReadyListener()
        self.addOnMessageListener()
        
    def addOnReadyListener(self):
        @self.client.event
        async def on_ready():
            print(f'{self.client.user} has connected to Discord!')
    
    
    def addOnMessageListener(self):    
        @self.client.event
        async def on_message(message):
            print(f"Message Received {message.content}")
            if message.author == self.client.user:
                print("Rajandingong")
                return

            if message.content.startswith('$hello'):
                await message.channel.send('Hello!')
                
                
    def start(self):
        self.client.run(self.token)                