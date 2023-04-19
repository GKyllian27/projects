import random
 
playing = True #mettre en False si vous ne jouez pas. 

list_of_games = ["Counter Strike : Globale Offensive", "Rocket League", "Fortnite"]


while True:
    random_game = random.choice(list_of_games)
    online_or_not = input(" Etes vous en ligne ? o/n : ")


    if online_or_not == "o" and playing == True:
        print(f"Vous êtes en ligne, vous jouez à {random_game}.")
    elif online_or_not == "o":
        print("Vous êtes en ligne.")
    else:
        print("Vous êtes hors ligne.") 