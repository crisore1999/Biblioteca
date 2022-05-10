class  Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore

    def toString(self):
        print("Autore: {}, Titolo: {}").format(self.autore, self.titolo)