# This a basic CLI calculator in Python
# All rights reserved © 2025, DESCOURS--TERRIER Benjamin
while True:
    Number_1 = float(input("A first number please ? "))
    Number_2 = float(input("A second number please ? "))
    Operation = input("What operation do you want to do ? 1. Addition; 2. Subtraction; 3. Multiplication; 4. Division; 5. Euclidean division: 6. Quit ")
    if Operation in ["1.", "Addition", "1", "addition"]:
        print("The result is", Number_1+Number_2)
    elif Operation in ["2.", "subtraction", "Subtraction", "2"]:
        print("The result is", Number_1-Number_2)
    elif Operation in ["3.", "multiplication", "Multiplication", "3"]:
        print("The result is", Number_1*Number_2)
    elif Operation in ["4.", "Division", "division", "4"]:
        print("The result is", Number_1/Number_2)
    elif Operation in ["5.", "euclidean division", "Euclidean division", "5"]:
        print("The result is", Number_1//Number_2, "and the rest is " ,Number_1%Number_2)    
    elif Operation in ["6.", "quit", "QUIT", "6"]:
        print("Goodbye")
        break
    else : print("Invalid operation")
