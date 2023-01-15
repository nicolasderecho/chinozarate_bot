class ContentFormatter():
    def __init__(self, message):
        self.raw_text = message or ""
        self.content = self.raw_text.strip()


class DiscordMessage():
    def __init__(self, application, trigger):
        self.trigger = trigger
        self.message = ContentFormatter(self.trigger.content)
        self.application = application