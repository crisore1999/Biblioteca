from biblio.Scaffale import Scaffale
from biblio.Libro import Libro
class Piano:
    def __init__(self):
        self.lista_scaffali = list()
        for x in range(30):
            self.lista_scaffali.append(Scaffale())

    def addScaffale(self, scaffale, ripiano, libro):
        self.lista_scaffali[scaffale - 1].addRipiano(ripiano, libro)

    def toString(self):
        stringa = "("
        for x in self.lista_scaffali:
            stringa += str(x)
        stringa += ")"
        return stringa
