import sys
import Personnage as Personnage
import Guerrier as Guerrier
import Mage as Mage
import Joueur as Joueur


def main():
    # print("Test primaire de la class personnage \n -------------")
    # personnage1 = Personnage.Personnage("toto")
    # print(personnage1)
    # print("|")
    # print("Test Setter et Getter \n -------------")
    # Personnage.Personnage.setPseudo(personnage1, "titi")
    # print(Personnage.Personnage.getPseudo(personnage1))
    # print("|")
    # print("Test création \n -------------")
    # Personnage.Personnage.creation(personnage1, "tata")
    # print(personnage1)
    # print("|")
    # print("Test création 2 \n -------------")
    personnage1 = Personnage.Personnage("toto")
    personnage1 = Personnage.Personnage.creation2(personnage1, 10, 10)
    # Personnage.Personnage.creation2(personnage1, "toto", 20)
    # print(personnage1)
    # personnage2 = Personnage.Personnage("titi")
    # Personnage.Personnage.creation2(personnage2, "titi", 15)
    # print(personnage2)
    # print("|")
    # print("Test attaque \n -------------")
    # Personnage.Personnage.attaque(personnage1, personnage2)
    # print("Test combat \n -------------")
    # Personnage.Personnage.combat(personnage1, personnage2)

    guerrier = Guerrier.Guerrier("toto", 5)
    #print(guerrier)

    mage = Mage.Mage("titi", 5)
    #print(mage)

    #print(Personnage.Personnage.combat(guerrier, mage))

    # Test Joueurs
    joueur1 = Joueur.Joueur("Martin", listePersonnage=[])
    joueur1.ajout(mage)
    joueur1.ajout(guerrier)
    print(joueur1)
    print(joueur1.getPersonnageIndex(0))
    #print(joueur1.getPersonnageIndex(1))
    print(joueur1.getPersonnageSearch("toto"))
    print(joueur1.getPersonnagePerso("Mage"))
    print(joueur1.afficherListe())
    print(joueur1.deletePersonnageIndex(1))
    print(joueur1.deletePersonnageSearch("toto"))
    print(joueur1.deletePersonnagePerso("Mage"))


if __name__ == '__main__':
    sys.exit(main())
