# ASCII code file 2
class ASCIICode2:
    def __init__(self):
        self.ascii_chars = "Hello World"
    
    def process_ascii(self, text):
        return text.encode('ascii').decode('ascii')
