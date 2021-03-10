import math

def task11(x, y):
     """
    Calculates and prints result of mathematical operations with two parameters
    :param x: First parameter
    :param y: Second parameter
    """
    a = math.pow(x, 3) - 23 * math.pow(y, 4)
    b = math.pow(y, 5) + math.log(y)
    c = (math.pow(y, 2) / 56) + math.cos(y) - 28
    d = 15 * math.pow(x, 7) - math.tan(y) + 19
    e = math.pow(y, 3) + math.pow(x, 8)
    result = (a / b)- c - math.sqrt(d / e)
    return result

print (task11 (x, y))

####################################################################################

def task12(x):
     """
    Calculates result of mathematical operations with one parameter depending on the specific conditions
    :param x: Parameter with which to operate
    """
    if x < 144:
        print(f"{function1(x):.2e}")

    if (x >= 144) and (x < 177):
        print(f"{function2(x):.2e}")

    if (x >= 177) and (x < 234):
        print(f"{function3(x):.2e}")

    if x >= 234:
        print(f"{function4(x):.2e}")

def function1(x):
     """
    Returns result of mathematical operations with one parameter
    :param x: Parameter with which to operate
    :return: Result of mathematical operations with one parameter
    """
	return math.pow(x, 3) - math.log(x)

def function2(x):
     """
    Returns result of mathematical operations with one parameter
    :param x: Parameter with which to operate
    :return: Result of mathematical operations with one parameter
    """
	return math.pow(x, 8) - math.log(x)

def function3(x):
    """
    Returns result of mathematical operations with one parameter
    :param x: Parameter with which to operate
    :return: Result of mathematical operations with one parameter
    """
	return math.pow(x, 5) / 56 + math.cos(x) - 28

def function4(x):
    """
    Returns result of mathematical operations with one parameter
    :param x: Parameter with which to operate
    :return: Result of mathematical operations with one parameter
    """
	return 84 * x - math.sin(x) + 56


##################################################################################
import math

def task13(n, m):

    print (f"{sum1(1, 1, n, m) + sum2(1, n, m):.2e}")


def sum1(i, j, n, m):

    result = 0.0
    for x in range(i, n + 1):
        for y in range(j, m + 1):
            result = result + (math.pow(i, 3) - 23 * math.pow(j, 4))
    return result


def sum2(i, n, m):

    result = 0.0
    for x in range(i, n + 1):
        result = result + (abs(i) + math.cos(i))
    return result

print (task13 (91, 23))

#############################################################################
import math

def task14(n):

    a = 0.0
    b = 0.0
    result = 8.0
    if n > 0:
        a = a + (1/89) * task14(n - 1)
        b = b + math.sin * task14(n - 1)
        result = a - b
    return result

print (task14 (14))

#############################################################################
