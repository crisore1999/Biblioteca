from biblio.Libro import Libro
class Ripiano:
    def __init__(self):
        self.libri = dict({})
        for x in range(1, 11):
            self.libri["Ripiano "+str(x)] = Libro("", "")

    def addLibro(self, nomeRipiano, titolo, autore):
        add_libro = Libro(titolo, autore)
        self.libri.update({"Ripiano": nomeRipiano, "Libro": add_libro})

    def toString(self):
        print("-----Lista Ripiani-----")
        for x in self.libri:
            print(x)