from biblio.Libro import Libro
class Ripiano:
    def __init__(self):
        self.libri = dict({})
        for x in range(1, 11):
            self.libri["Libro"+str(x)] = Libro("", "")

    def addLibro(self, nomeRipiano, titolo, autore):
        add_libro = Libro(titolo, autore)
        self.libri[nomeRipiano] = add_libro

    def toString(self):
        print("-----Lista Libri-----")
        for x in self.libri:
            print("Ripiano: {}, Titolo: {}, Autore: {}\n".format(self.libri[x], self.libri[x].titolo, self.libri[x].autore))