# UTF-8 code file 3
class UTF8Code3:
    def __init__(self):
        self.special_chars = "éñáüß"
        self.emoji = "🚀🎉🌟"
    
    def process_utf8(self, text):
        return text.encode('utf-8').decode('utf-8')
