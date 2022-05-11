from biblio.Biblioteca import Biblioteca
from biblio.Piano import Piano
from biblio.Scaffale import Scaffale
from biblio.Ripiano import Ripiano
from biblio.Libro import Libro
print('Hello git')

biblioteca = Biblioteca()
piano = Piano()
scaffale = Scaffale()
ripiano = Ripiano()
libro = Libro("Dante Alighieri", "Divina Commedia")
#biblioteca.contiene(piano, scaffale, ripiano)
biblioteca.addLibro(piano, scaffale, ripiano, "Dante Alighieri", "Divina Commedia")
print("")