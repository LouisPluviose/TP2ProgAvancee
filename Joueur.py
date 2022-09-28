import Personnage as Personnage


class Joueur():
    def __init__(self, nom: str = None, listePersonnage: list = None):
        self.__nom = nom
        self.__listePersonnage = listePersonnage

    def __str__(self):
        return f"Le joueur {self.__nom} prossède ces personnages suivants : {self.__listePersonnage}"

    def ajout(self, p: Personnage.Personnage):
        self.__listePersonnage.append(p)

    def getPersonnageIndex(self, index: int = 0):
        return self.__listePersonnage[index]

    def getPersonnageSearch(self, pseudo: str = None):
        for p in self.__listePersonnage:
            if p.getPseudo() == pseudo:
                return p
    
    def getPersonnagePerso(self, perso: str=None):
        for p in self.__listePersonnage:
            if p.__class__.__name__ == perso:
                return p

    def deleteIndex(self, index: int = None):
        self.__listePersonnage.remove(index)

    def deleteSearch(self, pseudo: str = None):
        for p in self.__listePersonnage:
            if p.getPseudo() == pseudo:
                self.__listePersonnage.remove(p)

    def deletePerso(self, perso: str=None):
        for p in self.__listePersonnage:
            if p.__class__.__name__ == perso:
                self.__listePersonnage.remove(p)

    