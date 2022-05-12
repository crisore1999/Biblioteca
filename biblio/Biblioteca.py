from biblio.Piano import Piano
from biblio.Libro import Libro
from biblio.Scaffale import Scaffale
class Biblioteca:
    def __init__(self):
        self.lista_piani = dict({})
        for x in range(1, 4):
            self.lista_piani["Piano"+str(x)] = Piano()

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

    def toString(self):
        print("----------Lista Piani-----------")
        for piani in self.lista_piani:
            print(piani, ":(\n", end=' ')
            for scaffali in self.lista_piani[piani].lista_scaffali:
                print('\t', scaffali, ':(', end='\t\n')
                for ripiani in self.lista_piani[piani].lista_scaffali[scaffali].lista_ripiani:
                    print('\t\t', ripiani, ':(', end='\t\n')
                    for libri in self.lista_piani[piani].lista_scaffali[scaffali].lista_ripiani[ripiani].libri:
                        print('\t\t\t', libri, ', ', end='\t\n')
                    print('\t\t\t)')
                print('\t\t)')
            print('\t)')