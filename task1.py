from data import dataset

#   Написати функцію, що зберігає інформацію про улюблену страву користувача у певній країні
#   Викликати функцію


def addUserDish(user_name, country, dish):
    if user_name in dataset.keys():
        if country in dataset[user_name].keys():
            dataset[user_name][country].add(dish)
        else:
            dataset[user_name][country]={dish}
    else:
        dataset[user_name]={country:{dish}}

print("Task 1")

#Додати нового користувача та страву у новій країні
addUserDish("BOB","new_country_1","apple_1")

#Додати існуючому користувачу нову країну з новою стравою
addUserDish("BOB","new_country_1","apple_2")

#Додати існуючому користувачу нову страву в існуючого країну
addUserDish("BOB","new_country_1","new_food")

print(dataset)


print("\n\n")