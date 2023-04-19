#PROJET JEU DU NOMBRE MYSTERE
import random

nb_mystere = random.randrange(6+1)
nb_essais = 5

print("*** Le jeu du nombre mystère ***")
print(f"Il te reste {nb_essais} essais")
reponse = input("Devine le nombre : ")

while not reponse.isdigit():
    print("Veuillez entrer un nombre valide.")
    reponse = input("Devine le nombre : ")
    continue


while True:
    if reponse != nb_mystere: nb_essais -= 1

    if nb_essais == 0:
        print(f"Vous avez perdu. Le nombre à trouver était : {nb_mystere}")
        break

    elif int(reponse) < nb_mystere:
        print(f"Le nombre mystère est PLUS GRAND que {reponse}")
        print(f"Il te reste {nb_essais} essais")
        reponse = input("Devine le nombre : ")

    elif int(reponse) > nb_mystere:
        print(f"Le nombre mystère est PLUS PETIT que {reponse}")
        print(f"Il te reste {nb_essais} essais")
        reponse = input("Devine le nombre : ")

    else:
        print(f"Vous avez gagné ! Le nombre mystère était bel et bien {nb_mystere} !")
        print(f"Vous avez terminé le jeu en {nb_essais} essais !")
        break