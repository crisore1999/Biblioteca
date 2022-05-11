from biblio.Piano import Piano
from biblio.Libro import Libro
class Biblioteca:
    def __init__(self):
        piano1, piano2, piano3 = Piano(), Piano(), Piano()
        self.lista_piani = (piano1, piano2, piano3)

    def contiene(self, piano, scaffale, ripiano):
        if ripiano.libri is not None:
            #print("C'è almeno un libro nel piano {}, scaffale {}, ripiano {}\n".format(piano.toString(), scaffale.toString(), ripiano.toString()))
            print("C'è almeno un libro nel ripiano")
        else:
            #print("Non è presente nessun libro nel piano {}, scaffale {}, ripiano {}\n".format(piano.toString(), scaffale.toString(), ripiano.toString()))
            print("Non c'è nessuno libro nel ripiano")

    def addLibro(self, piano, scaffale, ripiano, titolo, autore):
        add_libro = Libro(titolo, autore)
        self.lista_piani[piano - 1].addScaffale(scaffale, ripiano, add_libro)
