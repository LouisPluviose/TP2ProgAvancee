import Personnage as Personnage


class Guerrier(Personnage.Personnage):
    def __init__(self, pseudo: str = None, niveau: int = 1):
        super().__init__(pseudo, niveau)
        self.pseudo = pseudo
        self.pv = niveau * 5 + 10
        self.initiative = niveau * 6 + 4

    def __str__(self):
        return f"Le personnage {self.pseudo} est de la classe guerrier. \nIl a {self.pv} pv et {self.initiative} initiative"

    def degats(self):
        degats = self.getNiveau() * 2
        self.degats = degats
        return self.degats