from biblio.Ripiano import Ripiano
from biblio.Libro import Libro
class Scaffale:
    def __init__(self):
        self.lista_ripiani = dict({})
        for x in range(1, 7):
            self.lista_ripiani[("SC"+str(x))] = Ripiano()

    def addRipiano(self, ripiano, libro):
        self.lista_ripiani[ripiano-1].addLibro(libro)

    def toString(self):
        print("-----Lista Scaffali-----")
        for x in self.lista_ripiani:
            print(x)