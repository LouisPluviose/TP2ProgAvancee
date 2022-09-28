import Personnage as Personnage


class Mage(Personnage.Personnage):
    def __init__(self, pseudo: str = None , niveau: int = 1):
        super().__init__(pseudo, niveau)
        self.setPV = niveau * 8 + 4
        self.setInitiative = niveau * 4 + 6
        self.mana = niveau * 5

    def __str__(self):
        return f"Le personnage {self.getPseudo} est de la classe mage. \nIl a {self.getPV} pv, {self.getInitiative} initiative et {self.mana} de mana"

    def degats(self):
        if self.mana > 4:
            degats = self.getNiveau() + 3
            self.degats = degats
            return self.degats
        else:
            degats = self.getNiveau()
            self.degats = degats
            return self.degats