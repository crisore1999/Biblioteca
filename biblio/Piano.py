from biblio.Scaffale import Scaffale
from biblio.Libro import Libro
class Piano:
    def __init__(self):
        self.lista_scaffali = dict({})
        for x in range(1, 31):
            self.lista_scaffali["SC"+str(x)] = Scaffale()

    def addScaffale(self, scaffale, ripiano, libro):
        self.lista_scaffali[scaffale - 1].addRipiano(ripiano, libro)

    def toString(self):
        print("----------Lista Scaffali-----------")
        for x in self.lista_scaffali:
            print(x)
