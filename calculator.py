"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    input_string = input("Enter your question: ")
    tokens = input_string.split(' ')
    

    if tokens[0] in ['q', 'quit']:
        print("\nYou will exit")
        break
    else:
        if len(tokens) == 2:
            try:
                num1 = float(tokens[1])
            except ValueError:
                print("\nValue provided is not a number")
                continue
        else:
            try:
                num1 = float(tokens[1])
                num2 = float (tokens[2])
            except ValueError:
                print("One or more of the value(s) provided is not a number")
                continue


        if(tokens[0] == "+"):
            print(add(num1, num2))
        
        elif(tokens[0] == "-"):
            print(subtract(num1, num2))
        
        elif(tokens[0] == "*"):
            print(multiply(num1, num2))
        
        elif(tokens[0] == "/"):
            print(divide(num1, num2))

        elif(tokens[0] == "square"):
            print(square(num1))
        
        elif(tokens[0] == "cube"):
            print(cube(num1))
        
        elif(tokens[0] == "pow"):
            print(power(num1, num2))
        
        elif(tokens[0] == "mod"):
            print(mod(num1, num2))