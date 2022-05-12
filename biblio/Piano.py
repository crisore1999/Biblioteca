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
        for scaffali in self.lista_scaffali:
            print(scaffali, ":(\n", end=" ")
            for ripiani in self.lista_scaffali[scaffali].lista_ripiani:
                print('\t', ripiani, ":(", end="\t\n")
                for libri in self.lista_scaffali[scaffali].lista_ripiani[ripiani].libri:
                    print('\t\t', libri, ", ", end="\t\n")
                print("\t\t)")
            print("\t)")


