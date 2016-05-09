#ceasar cipher
#Jake Routh
#2/11/16

class CeasarCipher(object):

    def __init__(self):
        SOURCE = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        self.nCode = {}
        self.dCode = {}

        for i in range (len(SOURCE)):
            self.nCode[SOURCE[i]] = i
            self.dCode[i] = SOURCE[i]


    def encode(self, msg):
        out = []
        for letter in msg:
            code = self.nCode[letter]
            out.append(code)
        return out

    def decode(self, msg):
        out = ""
        for number in msg:
            code = self.dCode[number]
            out += code
        return out



