import math

def task11(x, y):
    a = math.pow(x, 3) - 23 * math.pow(y, 4)
    b = math.pow(y, 5) + math.log(y)
    c = (math.pow(y, 2) / 56) + math.cos(y) - 28
    d = 15 * math.pow(x, 7) - math.tan(y) + 19
    e = math.pow(y, 3) + math.pow(x, 8)
    result = (a / b)- c - math.sqrt(d / e)
    return result

print (task11 (17, 67))
