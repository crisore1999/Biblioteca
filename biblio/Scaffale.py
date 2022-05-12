from biblio.Ripiano import Ripiano
from biblio.Libro import Libro
class Scaffale:
    def __init__(self):
        self.lista_ripiani = dict({})
        for x in range(1, 7):
            self.lista_ripiani[("Ripiano"+str(x))] = Ripiano()

    def addRipiano(self, ripiano, libro):
        self.lista_ripiani[ripiano-1].addLibro(libro)

    def toString(self):
        print("-----Lista Ripiano-----")
        for ripiani in self.lista_ripiani:
            print(ripiani, ":(\n", end=" ")
            for libri in self.lista_ripiani[ripiani].libri:
                print('\t', libri, ", ", end="\t\n")
            print("\t)")
