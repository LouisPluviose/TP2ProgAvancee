import Personnage as Personnage


class Joueur():
    def __init__(self, nom: str = None, listePersonnage: list = None):
        self.__nom = nom
        self.__listePersonnage = listePersonnage

    def __str__(self):
        return f"Le joueur {self.__nom} prossède ces personnages suivants : {self.__listePersonnage}"

    def ajout(self, p: Personnage.Personnage):
        self.__listePersonnage.append(p)

    def delete(self, index: int = None):
        self.__listePersonnage.remove(index)

    def getPersonnage(self):
        return self.__listePersonnage

    def getPersonnageIndex(self, index: int = 0):
        return self.__listePersonnage[index]

