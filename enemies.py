
import random

def enemies():
    enemies=["prisoner", "prison guard", "policeman", "swat", "solider"]
    hp = [50, 75, 100, 125, 150]


    enemies_hp_dict = {}

    for i in range(len(enemies)):
        enemies_hp_dict[enemies[i]] = hp[i]
    print(f"you encountered a {random.choice(enemies)} ")


#enemies()

def weapons():
    weapons=["fists","baton","knife","pistol","shotgun","smg","m4","rpg"]
    dmg = [5,15,20,25,30,35,40,50,80]

    weapon_dmg_dict = {}
    for i in range(len(weapons)):
       weapon_dmg_dict[weapons[i]] = dmg[i]

    print(weapon_dmg_dict)

#weapons()


def budget():
    budget = 0

    print(f"you have {budget} $")
if input == "b":
    budget()
