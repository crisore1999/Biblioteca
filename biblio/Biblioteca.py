from biblio.Libro import Libro
from biblio.piano import piano
from biblio.scaffale import scaffale
from biblio.ripiano import ripiano
class Biblioteca:
    def __init__(self):
        self.piani = {"piano 1": scaffale, "piano 2": scaffale, "piano 3": scaffale}
        self.scaffali = {"scaffale 1": ripiano,
                         "scaffale 2": ripiano,
                         "scaffale 3": ripiano,
                         "scaffale 4": ripiano,
                         "scaffale 5": ripiano,
                         "scaffale 6": ripiano,
                         "scaffale 7": ripiano,
                         "scaffale 8": ripiano,
                         "scaffale 9": ripiano,
                         "scaffale 10": ripiano
                         "scaffale 11": ripiano
                         "scaffale 12": ripiano,
                         "scaffale 13": ripiano,
                         "scaffale 14": ripiano,
                         "scaffale 15": ripiano,
                         "scaffale 16": ripiano,
                         "scaffale 17": ripiano,
                         "scaffale 18": ripiano,
                         "scaffale 19": ripiano,
                         "scaffale 20": ripiano,
                         "scaffale 21": ripiano,
                         "scaffale 22": ripiano,
                         "scaffale 23": ripiano,
                         "scaffale 24": ripiano,
                         "scaffale 25": ripiano,
                         "scaffale 26": ripiano,
                         "scaffale 27": ripiano,
                         "scaffale 28": ripiano,
                         "scaffale 29": ripiano,
                         "scaffale 30": ripiano}
        self.libri = []
        self.ripiani = {"SC1": libri, "SC2": libri, "SC3": libri, "SC4": libri, "SC5": libri, "SC6": libri}

    def inserisciLibro(self, titolo, autore):
        add_libro = Libro(titolo, autore)
        self.libri.append(add_libro)

    def contiene(self, piano, scaffale, ripiano):
        if self.ripiani[piano][scaffale] == ripiano:
            

    def getLibri(self, piano, scaffale):
        pass

    def getPiano(self, libro):
        pass

    def getScaffale(self, libro):
        pass

    def getRipiano(self, libro):
        pass

    def cerca(self, autore, titolo):
        pass


