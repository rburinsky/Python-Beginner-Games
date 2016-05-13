"""
Test Python combat sim
Design Overview:

Each Cowboy get a chance to attack and hit
Requirements: Cowboys and Aliens fight to the death

Design mechanics:
cowboys:
health: 100
attack power: 35
percent hit: 0.5 or 50%

aliens:
health:  200
attack power:  20
percent hit: .2 or 20%

Functions

Testing

"""

import random

def attack(health, power, percent_to_hit):
    random_number = random.random()
    if random_number <= percent_to_hit:
        health = health - power
    return health

def simulate_army(number_of_cowboys=45, number_of_aliens=500):
    # cowboys:
   cowboy_starting_health = 100
   cowboy_attack_power = 35
   cowboy_percent_hit = 0.5


    # aliens:
   alien_starting_health = 200
   alien_attack_power = 20
   alien_percent_hit = 0.2

   #Initialize cowboys and aliens
   cowboy = cowboy_starting_health
   alien = alien_starting_health
   rounds = 0
   while(number_of_cowboys > 0 and number_of_aliens > 0):
        while(cowboy > 0 and alien > 0):
            rounds = rounds + 1
            cowboy = attack(cowboy, alien_attack_power, alien_percent_hit)
            alien = attack(alien, cowboy_attack_power, cowboy_percent_hit)
        if cowboy > 0:
            number_of_aliens = number_of_aliens - 1
            alien = alien_starting_health
        elif alien > 0:
            number_of_cowboys = number_of_cowboys - 1
            cowboy = cowboy_starting_health
        else:
            number_of_aliens = number_of_aliens - 1
            alien = alien_starting_health
            number_of_cowboys = number_of_cowboys - 1
            cowboy = cowboy_starting_health

    #testing remaning aliens and cowboys



        print ("Cowboys remaining:", number_of_cowboys)
        print ("Aliens remaining:", number_of_aliens)
        print ("Number of rounds:", rounds)
        print (cowboy, alien, rounds)


    #User input total number of cowboys and aliens
number_of_cowboys = input("How many cowboys? ")
number_of_aliens = input("How many aliens? ")

number_of_cowboys = int(number_of_cowboys)
number_of_aliens = int(number_of_aliens)

rerun = True

while rerun:
        simulate_army(number_of_cowboys, number_of_aliens)

        rerun = input("Rerun ([Y]/n)? ")
        if rerun.lower().startswith(("n", "q")):
            rerun = False
        else:
            rerun = True
