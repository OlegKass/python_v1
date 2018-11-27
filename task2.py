from data import dataset


#    Створити пакет validators та написати функції, що валідують усі дані. Імпорутвати дані функції.

from validators.lib import *

from task1 import addUserDish


#   Написати функцію, що зберігає інформацію про улюблену страву користувача у певній країні
#   Усі дані вводить користувач. Використати валідатори. Викликати функцію

def addUserDishValidator():
    #TODO
    number_of_pasport = getUserPassport()


    name_of_country = getCountryName()

    name_of_dish = getDishName()

    addUserDish(number_of_pasport, name_of_country, name_of_dish)

print("Task 2")
addUserDishValidator()
print(dataset)


print("\n\n")