class FakeMember():
    def __init__(self, id, name, **kwargs):
        self.id = id 
        self.name = name 
        self.bot = kwargs.get("bot", False)
        self.nick = kwargs.get("nick", None)
        self.mention = f"<@{self.id}>"