from biblio.Scaffale import Scaffale
class Piano:
    def __init__(self):
        self.lista_scaffali = list()
        for x in range(30):
            self.lista_scaffali.append(Scaffale())

    def addLibro(self, scaffale, ripiano, titolo, autore):
        add_libro = Libro(titolo, autore)
        self.lista_scaffali[scaffale - 1].addLibro(ripiano, add_libro)

    def toString(self):
        stringa = "("
        for x in self.lista_scaffali:
            stringa += str(x)
        stringa += ")"
        return stringa
