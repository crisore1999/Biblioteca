from biblio.Libro import Libro
class Biblioteca:
    def __init__(self):
        self.piani = {"Piano 1": self.scaffali, "Piano 2": self.scaffali, "Piano 3": self.scaffali}
        self.scaffali = {"SC1": self.ripiani,
                         "SC2": self.ripiani,
                         "SC3": self.ripiani,
                         "SC4": self.ripiani,
                         "SC5": self.ripiani,
                         "SC6": self.ripiani,
                         "SC7": self.ripiani,
                         "SC8": self.ripiani,
                         "SC9": self.ripiani,
                         "SC10": self.ripiani,
                         "SC11": self.ripiani,
                         "SC12": self.ripiani,
                         "SC13": self.ripiani,
                         "SC14": self.  ripiani,
                         "SC15": self.ripiani,
                         "SC16": self.ripiani,
                         "SC17": self.ripiani,
                         "SC18": self.ripiani,
                         "SC19": self.ripiani,
                         "SC20": self.ripiani,
                         "SC22": self.ripiani,
                         "SC23": self.ripiani,
                         "SC24": self.ripiani,
                         "SC25": self.ripiani,
                         "SC26": self.ripiani,
                         "SC27": self.ripiani,
                         "SC28": self.ripiani,
                         "SC29": self.ripiani,
                         "SC30": self.ripiani}
        self.ripiani = {"Ripiano 1": self.libri,
                        "Rpiano 2": self.libri,
                        "Ripiano 3": self.libri,
                        "Ripiano 4": self.libri,
                        "Ripiano 5": self.libri,
                        "Ripiano 6": self.libri}
        self.libri = []

    def inserisciLibro(self, titolo, autore):
        add_libro = Libro(titolo,autore)
        print("-----inserisci Libro------")
        self.libri.append(add_libro)
        print("Titolo: {}, Autore: {}\n").format(self.titolo, self.autore)

    def contiene(self, piano, scaffale, ripiano):
        pass



