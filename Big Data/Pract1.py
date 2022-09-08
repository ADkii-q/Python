import math

what = input("Фигуры: треугольник, прямоугольник, круг")

if what == "треугольник":
    d = float(input("Основание"))
    h = float(input("Высота"))
    S = (d * h) / 2
    print("Результат: " + str(S))
elif what == "прямоугольник":
    a = float(input("Сторона а"))
    b = float(input("Сторона б"))
    S = a * b
    print("Результат: " + str(S))
elif what == "круг":
    R = float(input("Радиус "))
    S = math.pi * math.pow(R, 2)
    print("Результат: " + str(S))
else:
    print("Выбрана неверная операция")
    
