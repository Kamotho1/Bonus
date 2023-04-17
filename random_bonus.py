#!/usr/bin/python3
import random
print("Python 3")

def random_bonus(hourly_rate):
    two = [2]*5
    five = [5]*2
    eight = [8]*2
    twelve = [12]*1
   
    bonus_list = two + five + eight + twelve

    number_of_hours = random.choice(bonus_list)
    bonus = hourly_rate * number_of_hours
    print("Your- Real bonus is: ", end="")
    print(bonus)

    for i in range(20):
        hours = random.choice(bonus_list)
        print("Bonus: ", i , " is: ", end="")
        bonus = hourly_rate * hours
        print(bonus)

random_bonus(10)



