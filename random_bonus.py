#!/usr/bin/python3
import random
print("Python 3")

def random_bonus(hourly_rate):
    two = [2,2,2,2,2]
    three = [3,3,3,3,3]
    four = [5,5,5]
    five = [2,2,2,2,2,2,2,2]
    six = [1,1,1,1,1,1,1,1,1,1,1,1]

    bonus_list = two + three + four + five + six

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



