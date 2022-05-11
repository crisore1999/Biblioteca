from biblio.Piano import Piano
class Biblioteca:
    def __init__(self):
        piano1, piano2, piano3 = Piano(), Piano(), Piano()
        self.lista_piani = (piano1, piano2, piano3)

    def contiene(self, piano, scaffale, ripiano):
        if ripiano[scaffale][piano] is not None:
            print("C'è almeno un libro nel ripiano {}").format(ripiano)
        else:
            print("Non è presente nessun libro nel ripiano {}").format(ripiano)



