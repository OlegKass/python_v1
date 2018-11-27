
from data import dataset
from task1 import *

#   Написати рекурсивну функцію, що повертає інформацію: хто і скільки улюблених страв у нього у кожній країні.
#   Рекурсивно необхідно пройтись по користувачам та по країнам.



def recursionByCountry(user_name,i=0):

    if user_name not in dataset.keys():
        return False
    list_of_dish=list(dataset[user_name][list(dataset[user_name][i])])
    if i >len(list_of_dish):
        return
    print(list(dataset[user_name][i]),len(list_of_dish))
    return recursionByCountry(user_name,i+1)
def recursionByUsers():
    #TODO


print("Task 3")

result = recursionByUsers()
print(result)

print("\n\n")



