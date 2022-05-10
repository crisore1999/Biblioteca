from biblio.Libro import Libro
class Ripiano:
    def __init__(self):
        self.libri = list()

    def aggiungiLibro(self, titolo, autore):
        add_libro = Libro(titolo, autore)
        self.libri.append(add_libro)