

import re

def getUserPassport():

    user_input = input("Enter number_of_pasport ")

    if (re.match(r"^[A-Z]{2}[0-9]{6}$", user_input) ):
        return user_input
    else:
        print("Enter correct infirmation")
        return getUserPassport()


"""
    Написати валідатор ....
    Правило валідації
"""

def getCountryName():
    user_input = input("Enter country name ")

    if (re.match(r"^[A-Z]{1}[a-z]{1,9}$", user_input) ):
        return user_input
    else:
        print("Enter correct infirmation" )
        return getCountryName()
"""
    Написати валідатор ....
    Правило валідації
"""


def getDishName():
    user_input = input("Enter food name ")

    if (re.match(r"^[A-Z]{1}[a-z]{1,9}$", user_input) ):
        return user_input
    else:
        print("Enter correct infirmation")
        return getDishName()

