class Face:

    def __init__(self, foto, blue, green, red, nome):
        self.foto = foto
        self.blue = blue
        self.green = green
        self.red = red
        self.nome = nome

    def setFoto(self, foto):
        self.foto = foto

    def setBlue(self, blue):
        self.blue = blue

    def setGreen(self, green):
        self.green = green

    def setRed(self, red):
        self.red = red

    def setNome(self, nome):
        self.nome = nome

    def getFoto(self):
        return self.foto

    def getBlue(self):
        return self.blue

    def getGreen(self):
        return self.green

    def getRed(self):
        return self.red

    def getNome(self):
        return self.nome
