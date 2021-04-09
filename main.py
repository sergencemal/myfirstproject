# This is a sample Python script.

from bmi import BMI

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    for i in range(15):
        print(age_calculator(i * i))

    bottle = Bottle("glass")
    bottle2 = Bottle("plastic")

    print("bottle type: " + bottle.type())
    print("bottle type: " + bottle2.type())


class Bottle:
    def __init__(self, bottle_type: str):
        self._bottle_type = bottle_type

    def type(self) -> str:
        return self._bottle_type


def age_calculator(age: int) -> str:
    if age >= 30:
        return "you old: " + str(age)
    else:
        return "you young: " + str(age)


def bmi_calculator():
    import numpy as np
    height = float(input('what is your height in m?'))
    check_datatype_height(height)
    weight = int(input('what is your weight in kg?'))
    check_datatype_weight(weight)
    height_person2 = float(input('what is your friends height in m?'))
    check_datatype_height(height_person2)
    weight_person2 = int(input('what is your friends weight in kg?'))
    check_datatype_weight(weight_person2)
    height_list = [float(height), float(height_person2)]
    weight_list = [int(weight), int(weight_person2)]
    height_list_np = np.array(height_list)
    weight_list_np = np.array(weight_list)
    bmi = weight_list_np/height_list_np**2
    print('person 1 your bmi is ' + str(bmi[0]))
    print('person 2 your bmi is ' + str(bmi[1]))


def check_datatype_height(self):
    while type(self) == str:
        if type(self) is str:
            print('input incorrect')
            self = input('what is your height in m?')
        elif type(self) is bool:
            print('input incorrect')
            self = input('what is your height in m?')


def check_datatype_weight(self):
    while type(self) == str or bool:
        if type(self) is str:
            print('input incorrect')
            self = input('what is your height in kg?')
        elif type(self) is bool:
            print('input incorrect')
            self = input('what is your height in kg?')
        break


def is_float(input) -> bool:
    try:
        float(input)
        return True
    except ValueError:
        return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        height = input("What is your height in cm? ")
        if is_float(height):
            break

    while True:
        weight = input("What is your weight in kg? ")
        if is_float(weight):
            break

    try:
        bmi = BMI(height, weight)
        print("Your BMI is: ")
        print(bmi.calculate())
        print(bmi.category())
    except ValueError:
        print("One of the values was the wrong type")

    for i in range(1,49,3):
        print(i)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import numpy as np
# my_list = [2, 5, 6, 9]
# divider = [3, 5, 8, 9]
# my_list[1] = 3
# divider[3] = 3
# my_list.append(30)
# divider.append(10)
# my_list.reverse()
# print(my_list)
# print(divider)
# my_list_np = np.array(my_list)
# divider_np = np.array(divider)
# newlist = my_list_np/divider_np
# print(newlist)
# name_uppercase = ('MEHMET')
# print(name_uppercase.count('E'))
# name_uppercase_lower = name_uppercase.lower()
# print(name_uppercase_lower)
