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
=======( 4 )=========( Реализовать рекуррентную функцию )=================================
import math


def f14(n: object) -> float:
    a = 0
    b = 0
    if n == 0:
        return 8
    else:
        a = a + (1 / 89) * f14(n - 1)
        b = b + math.sin(f14(n - 1))
        return a - b
print(f14(13))
=======( 2.1 )=========( Реализовать функцию­дерево решений )=================================
def f21(x):
    if x[0] == 1969:
        return 11
    if x[0] == 2019:
        if x[2] == 1976:
            return 10
        if x[2] == 1990:
            return 9
        if x[2] == 1977:
            if x[3] == 1978:
                return 6
            if x[3] == 2020:
                return 7
            if x[3] == 1993:
                return 8
    if x[0] == 1973:
        if x[2] == 1990:
            return 2
        if x[2] == 1976:
            if x[3] == 1978:
                return 3
            if x[3] == 2020:
                return 4
            if x[3] == 1993:
                return 5
        if x[2] == 1977:
            if x[1] == 2020:
                return 0
            if x[1] == 1976:
                return 1

print (f21([1969, 2020, 1976, 1993]))
=======( 2.2 )=========( Реализовать функцию­транскодер из формата )=================================
def f22(x) -> int:

    a = x & 0b00000000000000000001111111111111
    b = x & 0b00000000000001111110000000000000
    c = x & 0b01111111111110000000000000000000
    d = x & 0b10000000000000000000000000000000

    a = a << 6
    b = b >> 13
    c = c << 1
    d = d >> 12

    return hex(a | b | c | d)

print(f22(0xa441eb39))
=======( 3.2 )=========( класс C32 )============================================
class C32:

    def __init__(self):
        self.state = 'A'

    def rig(self):
        if self.state == 'A':
            self.state = 'G'
            return 1
        elif self.state == 'B':
            self.state = 'E'
            return 4
        elif self.state == 'C':
            self.state = 'E'
            return 6
        elif self.state == 'E':
            self.state = 'F'
            return 8
        else:
            return RuntimeError

    def amble(self):
        if self.state == 'A':
            self.state = 'E'
            return 2
        if self.state == 'C':
            self.state = 'D'
        else:
            return RuntimeError

    def click(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'C'
            return 3
        if self.state == 'D':
            self.state = 'E'
            return 7
        if self.state == 'F':
            self.state = 'G'
            return 9
        else:
            return RuntimeError
