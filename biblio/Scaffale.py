from biblio.Ripiano import Ripiano
class Scaffale:
    def __init__(self):
        ripiano1, ripiano2, ripiano3, ripiano4, ripiano5, ripiano6 = Ripiano()
        self.ripiani = list(ripiano1, ripiano2, ripiano3, ripiano4, ripiano5, ripiano6)
