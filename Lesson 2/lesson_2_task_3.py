import math

def square(side):
    area = side ** 2
    area = math.ceil(area)
    return area

side = float(input("Введите длину стороны квадрата: "))
print("Площадь квадрата:", square(side))