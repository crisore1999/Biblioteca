from biblio.Scaffale import Scaffale
class Piano:
    def __init__(self):
        self.lista_scaffali = list()
        for x in range(30):
            self.lista_scaffali.append(Scaffale())

