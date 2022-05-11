from biblio.Libro import Libro
class Ripiano:
    def __init__(self):
        self.libri = list()
        for x in range(10):
            self.libri.append(Libro)

    def addLibro(self, titolo, autore):
        add_libro = Libro(titolo, autore)
        self.libri.append(add_libro)

    def toString(self):
        stringa = "("
        for x in self.libri:
            stringa += str(x)
        stringa += ")"
        return stringa