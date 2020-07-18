"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    input_string = input("Enter your question: ")
    tokens = input_string.split(' ')
    num1 = float(tokens[1])
    num2 = float (tokens[2])

    if tokens[0] == 'q':
        print("You will exit")
        break
    else:
        if(tokens[0] == "+"):
            print(add(num1, num2))