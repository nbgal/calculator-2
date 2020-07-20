"""Functions for common math operations."""


def add(num):
    """Return the sum of the two input integers."""
    sum = 0

    for i in range (len(num)):
        sum += num[i]
    return sum


def subtract(num):
    """Return the second number subtracted from the first."""
    temp = num[0]
    for i in range (1, len(num)):
        temp -= num[i]
        
    return temp


def multiply(num):

    """Multiply the two inputs together."""
    temp = num[0]
    for i in range (1, len(num)):
        temp *= num[i]
    
    return temp


def divide(num):
    """Divide the first input by the second and return the result."""
    
    temp = num[0]
    for i in range (1, len(num)):
        temp /= num[i]
    
    return temp



def square(num):
    """Return the square of the input."""

    return num[0]*num[0]


def cube(num):
    """Return the cube of the input."""

    return num[0] * num[0] * num[0]


def power(num):
    """Raise num1 to the power of num2 and return the value."""
    
    temp = num[0]
    for i in range (1, len(num)):
        temp **= num[i]
    
    return temp



def mod(num):
    """Return the remainder of num1 / num2."""
    temp = num[0]
    for i in range (1, len(num)):
        temp %= num[i]
    return temp



def add_mult(num):
    """ Return the sum of num1 and num 2 multiplied by num3"""
    print(num)
    value =[]
    value.append(add(num[0:2]))
    print(value)
    for i in range (2,len(num)):
        print(len(num))
        print (num[i])
        value.append(num[i]) 
        print(value)

    return multiply(value)


def add_cubes(num):
    """Return the sum of the cube of both numbers"""
    val = 1
    sum = 0

    for i in range(len(num)):
        val = cube([num[i]])
        sum += val

    return sum