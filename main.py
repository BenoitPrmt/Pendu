from pendu import pendu_model
from functions import select_word

mot = select_word.select_word()
affichage = "_" * len(mot)
pendu = 0

print("_______________________________________\n")
print("Bienvenue au jeu du pendu !")
print("Le mot à deviner contient {} lettres".format(len(mot)))
print("Vous avez droit à 8 essais")
print("Bonne chance !")
print("Pendu by @BenoitPrmt")
print("_______________________________________\n")


while True:
    print("Mot à trouver : " + affichage)
    print("_______________________________________\n")

    lettre = input("Entrez une lettre : ")

    if len(lettre) > 1:
        print("Vous ne pouvez entrer qu'une seule lettre\n")
        continue

    if lettre in mot and lettre not in affichage:
        indice = mot.index(lettre)
        
        for d in range(mot.count(lettre)):
            indice = mot.index(lettre, indice)
            affichage = affichage[:indice] + lettre + affichage[indice+1:]
            indice += 1
    else:
        print("Lettre non présente dans le mot\n")
        pendu += 1

        for i in range(pendu):
            print(pendu_model[i])
        
        print("\n")

        if pendu == 8:
            print("\tPerdu ! Le mot était {} !".format(mot))
            break

    print("Il vous reste {} essais\n".format(8 - pendu))

    if "_" not in affichage:
        print("\tBravo ! Le mot était bien {} !".format(mot))
        break

    