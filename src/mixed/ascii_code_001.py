# ASCII code file 1
class ASCIICode1:
    def __init__(self):
        self.ascii_chars = "Hello World"
    
    def process_ascii(self, text):
        return text.encode('ascii').decode('ascii')
