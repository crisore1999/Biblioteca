
class  Libro:
    def __init__(self, titolo: str, autore: str):
        self.titolo = titolo
        self.autore = autore

    def toString(self):
        print("----------Stampa Libro----------")
        print("Autore: {}, Titolo: {}\n".format(self.autore, self.titolo))