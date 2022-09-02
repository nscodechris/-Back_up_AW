
import random
# simulating getting hit by the enemies
# getting attack twice; attack = random 20 to 30
# after attack you pick up a potion
# when adding health add 10 + random  10 to 15
# finish with print the players health

health = 100
heal_potion = 10
potion = random.randint(10, 15)
monster_attack = random.randint(20, 30)
attack_count = 1
i = 2


print(f"Welcome Hero!, your HP is {health}")
print("----------------------------------------------------------------------------------------------------")
print("As you enter the forest of great mystery you come upon the evil from within!!\nIt attacks you right away")
print("The monster will attack you twice!!")
input("press enter")
print("----------------------------------------------------------------------------------------------------")
while i != 0:
    print("First Fight" if attack_count == 1 else "Second fight")
    input("press enter")
    print("----------------------------------------------------------------------------------------------------")
    health = health - monster_attack
    print(f"After the attack you have: \nHP {health}")
    print("----------------------------------------------------------------------------------------------------")
    i -= 1
    attack_count += 2

dice_potion = input("You found a potion, roll a dice to see how much health you will gain\npress enter to roll:")
health = health + heal_potion + potion
print(f"The potion you received gave you {potion + heal_potion} HP, your HP is now {health}")
print("Thank you for playing")
print("----------------------------------------------------------------------------------------------------")
