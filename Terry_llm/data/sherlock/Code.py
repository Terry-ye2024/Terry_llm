class Code:
    def __init__(self, stoi, itos):
        self.stoi = stoi
        self.itos = itos

    def encode(self, s):
        return [self.stoi[c] for c in s] # encoder: take a string, output a list of integers
    def decode(self, l):
        return ''.join([self.itos[i] for i in l]) # decoder: take a list of integers, output a string