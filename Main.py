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
biblioteca.contiene(piano, scaffale, ripiano)
#ripiano.addLibro("Ripiano 1", "Dante Alighieri", "Divina Commedia")
ripiano.addLibro("Ripiano 2", "Giovanni Verga", "Rosso Malpelo")
piano.toString()
scaffale.toString()
ripiano.toString()
libro.toString()
#biblioteca.addLibro(piano, scaffale, ripiano, "Dante Alighieri", "Divina Commedia")
print("")