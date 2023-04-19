#PROJET JEU DE ROLE
import random

choice_user = input("Souhaitez-vous attaquer ⚔ (1) ou utiliser une potion 🧪 (2) ? ")

enemy_life = 50
user_life = 50
number_of_potions = 3

while not choice_user.isdigit():
    print("Attaquer pour (1) et se soigner pour (2) !")
    choice_user = input("Souhaitez-vous attaquer ⚔ (1) ou utiliser une potion 🧪 (2) ? ")
    continue

while True:

    damage_to_enemy = random.randint(5, 10)
    damage_received = random.randint(5, 15)
    potion_points = random.randint(15, 50)

    #𝙏𝙤 𝙖𝙩𝙩𝙖𝙘𝙠
    if choice_user == "1":
        user_life -= damage_received
        enemy_life -= damage_to_enemy
        print(f"Vous avez infligé {damage_to_enemy} points de ⚔ ")
        print(f"L'ennemi vous a infligé {damage_received} points de ❤️")
        #𝙒𝙞𝙣 𝙤𝙧 𝙇𝙤𝙤𝙨𝙚 
        if enemy_life <= 0:
            print("Tu as gagné 👊")
            break
        elif user_life <= 0:
            print("Tu as perdu... 💀")
            break
        print(f"VOUS : Il vous reste {user_life} points de ❤️")
        print(f"ENNEMI : Il reste {enemy_life} point de ❤️  à l'ennemi.")
        print("________________________________________________________________")
        choice_user = input("Souhaitez-vous attaquer ⚔ (1) ou utiliser une potion 🧪 (2) ? ")

    #𝙏𝙤 𝙝𝙚𝙖𝙡 𝙞𝙛 𝙥𝙤𝙩𝙞𝙤𝙣𝙨 𝙏𝙧𝙪𝙚
    elif choice_user == "2" and number_of_potions > 0:
        user_life -= damage_received
        user_life += potion_points
        number_of_potions -= 1
        print(f"Vous récupérez {potion_points} points de ❤️  ({number_of_potions} 🧪 restantes)")
        print(f"L'ennemi vous a infligé {damage_received} points de ❤️")
        print(f"VOUS : Il vous reste {user_life} points de ❤️")
        print("""________________________________________________________________\n 
        Vous passez votre tour...""")
        choice_user = input("Souhaitez-vous attaquer ⚔ (1) ou utiliser une potion 🧪 (2) ? ")

    #𝘾𝙖𝙨𝙚 𝙬𝙞𝙩𝙝𝙤𝙪𝙩 𝙥𝙤𝙩𝙞𝙤𝙣𝙨
    elif choice_user == "2" and number_of_potions <= 0:
        user_life -= damage_received
        print("Vous n'avez plus de 🧪...")
        print(f"L'ennemi vous a infligé {damage_received} points de ❤️")
        print(f"VOUS : Il vous reste {user_life} points de ❤️")
        print("""________________________________________________________________\n 
        Vous passez votre tour...""")
        choice_user = input("Souhaitez-vous attaquer ⚔ (1) ou utiliser une potion 🧪 (2) ? ")

    else:
        choice_user = input("Souhaitez-vous attaquer ⚔ (1) ou utiliser une potion 🧪 (2) ? ")