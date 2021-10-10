=======( 2 )=========( Реализовать кусочно линейную функцию )=============================
import math

def f12(x):
    if x < 144:
        return result1(x)
    if 144 <= x < 177:
        return result2(x)
    if 177 <= x < 234:
        return result3(x)
    if x >= 234:
        return result4(x)

def result1(x):
    return pow(x, 3) - math.log10(x)
def result2(x):
    return pow(x, 8) - math.log10(x)
def result3(x):
    return (pow(x, 5) / 56) + math.cos(x) - 28
def result4(x):
    return 84 * x - math.sin(x) + 56
print(f12(91))

=======( 3 )=========( Реализовать итерационную функцию )=================================
import math

def f13(n, m) -> float:
    return sum1(1, 1, n, m) + sum2(1, n)

def sum1(i, j, n, m) -> float:
    result = 0.0
    for x in range(i, n + 1):
        for y in range(j, m + 1):
            result = result + (pow(x, 3) - 23 * pow(y, 4))
    return result

def sum2(i, n) -> float:
    result = 0.0
    for x in range(i, n + 1):
        result = result + (math.fabs(x) + math.cos(x))
    return result

print(f13(91, 23))
