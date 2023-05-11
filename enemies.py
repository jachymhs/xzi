#dodelat fajtení s kostkama

import keyboard

def weapons():

    weapons=["fists","baton","knife","pistol","shotgun","smg","m4","rpg"]

    return weapons

def enemies_hp():
    import random
    enemies=["prisoner", "prison guard", "policeman", "swat", "solider"]
    enemy_weapons = ["baton", 75, 100, 125, 150]
    weapons()

    enemies_hp_dict = {}

    for i in range(len(enemies)):
        enemies_hp_dict[enemies[i]] = enemy_weapons[i]
    equiped_weapon = random.choice(weapons())

    print(f"you encountered a {random.choice(enemies)}  and you have {equiped_weapon}")


    equiped_weapons_dict = {"fists": 20, "baton": 18, "knife": 16, "pistol": 14, "shotgun": 12, "smg": 10, "m4": 8, "rpg": 6}
    #enemy_weapons_dict = {"prisoner":"baton","prison guard": "pistol","policeman":, "pistol": 14, "shotgun": 12, "smg": 10, "m4": 8, "rpg": 6}

    #bojovani
    def fight():
    #vystetlit kostku
        hrana = equiped_weapons_dict[equiped_weapon]
        print(f"Press 'f' to fight or 'e' to escape. The {equiped_weapon} grants you a {hrana} sided dice" )
        while True:
            if keyboard.is_pressed('f'):
                print("You are going to fight him.")
                kostka1 = (random.randint(1,hrana))
                print(f"you got a {kostka1} on your the dice")
                if kostka1 > 5:
                    print("you got your ass kicked and ran away")

                if kostka1 <= 5:
                    print("you killed him, great!")
                return False


            elif keyboard.is_pressed('e'):
                print("You escaped the fight.")
                return True
            else:
                pass

    fight()
    return enemies

enemies_hp()





    enemies_dmg_dict = {}

    for i in range(len(enemies)):
        enemies_dmg_dict[enemies[i]] = dmg[i]

#enemies_dmg()



















#def budget():
    budget = 0
    print(f"you have {budget} $")
