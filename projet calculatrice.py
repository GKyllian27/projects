#PROJET CALCULATRICE

premier_nb = input("Quel est votre premier nombre ? : ")

while premier_nb.isdigit() == False:
    print("Saisissez uniquement un nombre, pas de lettre !")
    premier_nb = input("Quel est votre premier nombre ? : ")
else:
    premier_nb = int(premier_nb)




deuxieme_nb = input("Quel est votre deuxieme nombre ? : ") 

while deuxieme_nb.isdigit() == False:
    print("Saisissez uniquement un nombre, pas de lettre !")
    deuxieme_nb = input("Quel est votre deuxieme nombre ? : ")
else:
    deuxieme_nb = int(deuxieme_nb)




methode_calcul = input("Que voulez-vous faire ? (+, -, /, *) : ")

liste_charact = ['+', '-', '*', '/']
while not methode_calcul in liste_charact:
    print("Donnez simplement le symbole correspondant à votre demande (+, -, *, /).")
    methode_calcul = input("Que voulez-vous faire ? (+, -, /, *) : ")




if methode_calcul == "+":
    print(f"le résultat de {premier_nb} + {deuxieme_nb} est égal à {premier_nb + deuxieme_nb}.")
elif methode_calcul == "-":
    print(f"le résultat de {premier_nb} - {deuxieme_nb} est égal à {premier_nb - deuxieme_nb}.")
elif methode_calcul == "/":
    print(f"le résultat de {premier_nb} divisé par {deuxieme_nb} est égal à {premier_nb / deuxieme_nb}.")
elif methode_calcul == "*":
    print(f"le résultat de {premier_nb} multiplié par {deuxieme_nb} est égal à {premier_nb * deuxieme_nb}.")