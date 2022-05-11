from biblio.Ripiano import Ripiano
class Scaffale:
    def __init__(self):
        self.lista_ripiani = dict({})
        for x in range(1, 7):
            self.lista_ripiani[("SC"+str(x))] = Ripiano()
