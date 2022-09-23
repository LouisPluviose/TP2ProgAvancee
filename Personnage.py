class Personnage:
    # Initialisation et str de la classe
    def __init__(self, pseudo: str = None, niveau: int = 1):
        self.__pseudo = pseudo
        self.__niveau = niveau
        self.__pv = niveau
        self.__initiative = niveau

    def __str__(self):
        return f"Le personnage {self.__pseudo}, est de niveau {self.__niveau} (pv : {self.__pv}, initiative {self.__initiative})"

    # Setter et Getter

    def getPseudo(self) -> str:
        return self.__pseudo

    def setPseudo(self, nouveauPseudo):
        self.__pseudo = nouveauPseudo

    def getPV(self) -> int:
        return self.__pv

    def setPV(self, nouveauPV):
        self.__pv = nouveauPV

    def getNiveau(self) -> int:
        return self.__niveau

    def getInitiative(self) -> int:
        return self.__initiative

    def setInitiative(self, nouvelleInitiative):
        self.__initiative = nouvelleInitiative

    # Constructeurs

    def creation(self, pseudoCreation):
        self.__pseudo = pseudoCreation

    def creation2(self, pseudoCreation, niveau):
        self.__pseudo = pseudoCreation
        self.__niveau = niveau
        self.__pv = niveau
        self.__initiative = niveau

    # Méthodes

    def attaque(self, opposant):
        if self.__initiative > opposant.__initiative:
            pv1 = opposant.__pv - self.degats()
            print(self.__pseudo, "fait", self.__niveau, "de dégâts à", opposant.__pseudo)
            print("pv restant de", opposant.__pseudo, " : ", pv1)
            opposant.__pv = pv1
            if pv1 > 0:
                pv2 = self.__pv - opposant.degats()
                print(opposant.__pseudo, "fait", opposant.__niveau, "de dégâts à", self.__pseudo)
                print("pv restant de", self.__pseudo, " : ", pv2)
                self.__pv = pv2
            else:
                print(opposant.__pseudo, "mort")
                opposant.__pv = 0
        elif self.__initiative > opposant.__initiative:
            pv3 = self.__pv - opposant.degats()
            print(opposant.__pseudo, "fait", {opposant.__niveau}, "de dégâts à", self.__pseudo)
            print("pv restant de", {self.__pseudo}, " : ", pv3)
            self.__pv = pv3
            if pv3 > 0:
                pv4 = opposant.__pv - self.degats()
                print(self.__pseudo, "fait", {self.__niveau}, "de dégâts à", opposant.__pseudo)
                print("pv restant de", opposant.__pseudo, " : ", pv4)
                opposant.__pv = pv4
            else:
                print(self.__pseudo, "mort")
        elif self.__initiative == opposant.__initiative:
            pv5 = opposant.__pv - self.degats()
            pv6 = self.__pv - opposant.degats()
            opposant.__pv = pv5
            self.__pv = pv6
            print("Attaque au même temps", opposant.__pseudo, "attaque", self.__pseudo, "et inversement")
            print(self.__pseudo, "fait", {self.__niveau}, "de dégâts à", opposant.__pseudo)
            print("pv restant de", opposant.__pseudo, " : ", pv5)
            print(opposant.__pseudo, "fait", {opposant.__niveau}, "de dégâts à", self.__pseudo)
            print("pv restant de", self.__pseudo, " : ", pv6)
            if pv5 < 0:
                print(opposant.__pseudo, "est mort")
                opposant.__pv = 0
            elif pv6 < 0:
                print(self.__pseudo, "est mort")
                self.__pv = 0

    def combat(self, opposant):
        while opposant.__pv > 0 and self.__pv > 0:
            print(Personnage.attaque(self, opposant))

    def soin(self):
        print()
        self.__pv = self.__pv + self.__niveau
        print(self.__pseudo, "il a maintenant", self.__pv, "points de vie")

    def degats(self):
        degats = self.getNiveau()
        self.__degats = degats
        return self.__degats