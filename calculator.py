"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    num = []
    input_string = input("Enter your question: ")
    tokens = input_string.split(' ')
    
    if tokens[0] in ['q', 'quit']:
        print("\nYou will exit")
        break
    else:
        try:
            for i in range (1,len(tokens)):
                num.append(float(tokens[i]))      
        except ValueError:
            print("\n One or more of the value(s) provided is not a number")
            continue


        if(tokens[0] == "+"):
            print(add(num))

        elif(tokens[0] == "-"):
            print(subtract(num))
        
        elif(tokens[0] == "*"):
            print(multiply(num))
        
        elif(tokens[0] == "/"):
            print(divide(num))

        elif(tokens[0] == "square"):
            print(square(num))
        
        elif(tokens[0] == "cube"):
            print(cube(num))
        
        elif(tokens[0] == "pow"):
            print(power(num))
        
        elif(tokens[0] == "mod"):
            print(mod(num))