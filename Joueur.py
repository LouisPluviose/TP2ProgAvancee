import Personnage as Personnage
import pickle
import json


class Joueur():
    def __init__(self, nom: str = None, listePersonnage: list = None):
        self.__nom = nom
        self.__listePersonnage = listePersonnage

    def __str__(self):
        return f"Le joueur {self.__nom} prossède ces personnages suivants : {self.__listePersonnage}"

    def ajout(self, p: Personnage.Personnage):
        if len(self.__listePersonnage) > 5:
            print("Vous avez atteint le nombre maximum de personnage")
        else:
            self.__listePersonnage.append(p)

    # afficher les stats de tout les personnages

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

    def afficherListe(self):
        for p in self.__listePersonnage:
            print(p)

    # supprimer un ou des personnages

    def deletePersonnageIndex(self, index: int):
        if index < len(self.__listePersonnage):
            self.__listePersonnage.pop(index)
            print(f"Le personnage {index} a été supprimé")

    def deletePersonnageSearch(self, pseudo: str = None):
        for p in self.__listePersonnage:
            if p.getPseudo() == pseudo:
                print(f"Le personnage {pseudo} a été supprimé")
                self.__listePersonnage.remove(p)

    def deletePersonnagePerso(self, perso: str = None):
        for p in self.__listePersonnage:
            if p.__class__.__name__ == perso:
                print(f"Le personnage {perso} a été supprimé")
                self.__listePersonnage.remove(p)

    # save and load in json
    def save(self):
        # serialization
        output = json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        # output
        with open("save.json", "w") as f:
            f.write(output)
            f.close()

    def load(self):
        with open('save.json', 'r') as infile:
            self.__dict__ = json.load(infile)