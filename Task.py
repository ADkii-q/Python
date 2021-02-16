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
