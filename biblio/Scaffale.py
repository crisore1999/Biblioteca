from biblio.Ripiano import Ripiano
class Scaffale:
    def __init__(self):
        self.lista_ripiani = dict({})
        for x in range(1, 7):
            self.lista_ripiani[("SC"+str(x))] = Ripiano()

    def addLibro(self, ripiano, titolo, autore):
        add_libro = Libro(titolo, autore)
        self.lista_ripiani[ripiano-1].addLibro(add_libro)

    def toString(self):
        stringa = "("
        for x in self.lista_ripiani:
            stringa += str(x)
        stringa += ")"
        return stringa