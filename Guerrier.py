import Personnage as Personnage


class Guerrier(Personnage.Personnage):
    def __init__(self, pseudo: str = None, niveau: int = 1):
        super().__init__(pseudo, niveau)
        self.setPV = niveau * 5 + 10
        self.setInitiative = niveau * 6 + 4

    def __str__(self):
        return f"Le personnage {Personnage.Personnage.getPseudo} est de la classe guerrier. \nIl a {Personnage.Personnage.getPV} pv et {Personnage.Personnage.getInitiative} initiative"

    def degats(self):
        degats = self.getNiveau() * 2
        self.degats = degats
        return self.degats