import math

what = input("Фигуры: Задание 1, Задание 2, Задание 3")

if what == "1":
    what = input("Фигуры: треугольник, прямоугольник, круг")
    if what == "треугольник":
        d = float(input("Основание "))
        h = float(input("Высота "))
        S = (d * h) / 2
        print("Результат: " + str(S))
    elif what == "прямоугольник":
        a = float(input("Сторона а "))
        b = float(input("Сторона б "))
        S = a * b
        print("Результат: " + str(S))
    elif what == "круг":
        R = float(input("Радиус "))
        S = math.pi * math.pow(R, 2)
        print("Результат: " + str(S))
    else:
        print("Выбрана неверная операция")

if what == "2":
    what = input("Операции: +, -, /, //, модуль, степень")
    a = float(input("число 1 "))
    b = float(input("число 2 "))
    if what == "+":
        Res = a + b
        print("Результат: " + str(Res))
    elif what == "-":
        Res = a - b
        print("Результат: " + str(Res))
    elif what == "/":
        Res = a / b
        print("Результат: " + str(Res))
    elif what == "//":
        Res = a // b
    elif what == "модуль":
        Res = math.fabs(a), math.fabs(b)
        print("Результат: " + str(Res))
    elif what == "степень":
        Res = math.pow(a, b)
        print("Результат: " + str(Res))
    else:
        print("Выбрана неверная операция")

if what == "3":
    what = input("Операции: формула Герона")
    a = float(input("Сторона 1 "))
    b = float(input("Сторона 2 "))
    c = float(input("Сторона 3 "))
    p = ((a+b+c) / 2)
    Res = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("Результат: " + str(Res))
