from biblio.Libro import Libro
class Biblioteca:
    def __init__(self):
        self.piani = {"Piano 1": scaffali, "Piano 2": scaffali, "Piano 3": scaffali}
        self.scaffali = {"SC1": ripiani,
                         "SC2": ripiani,
                         "SC3": ripiani,
                         "SC4": ripiani,
                         "SC5": ripiani,
                         "SC6": ripiani,
                         "SC7": ripiani,
                         "SC8": ripiani,
                         "SC9": ripiani,
                         "SC10": ripiani,
                         "SC11": ripiani,
                         "SC12": ripiani,
                         "SC13": ripiani,
                         "SC14": ripiani,
                         "SC15": ripiani,
                         "SC16": ripiani,
                         "SC17": ripiani,
                         "SC18": ripiani,
                         "SC19": ripiani,
                         "SC20": ripiani,
                         "SC22": ripiani,
                         "SC23": ripiani,
                         "SC24": ripiani,
                         "SC25": ripiani,
                         "SC26": ripiani,
                         "SC27": ripiani,
                         "SC28": ripiani,
                         "SC29": ripiani,
                         "SC30": ripiani}
        self.ripiani = {"Ripiano 1": libri,
                        "Rpiano 2": libri,
                        "Ripiano 3": libri,
                        "Ripiano 4": libri,
                        "Ripiano 5": libri,
                        "Ripiano 6": libri}
        self.libri = []

    def inserisciLibro(self, titolo, autore):
        add_libro = Libro(titolo,autore)
        print("-----inserisci Libro------")
        self.libri.append(add_libro)
        print("Titolo: {}, Autore: {}\n").format(self.titolo, self.autore)

    def contiene(self, piano, scaffale, ripiano):
        pass



