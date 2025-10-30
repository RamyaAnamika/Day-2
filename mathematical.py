
#print(f"enter the first num{}")
#print(f"enter the second num{num2}")
while True:
    opration=(input("What type of operation (+, -, *, /): "))

    if opration == "exit":
        print("Exiting the calculator. Goodbye!")
        break 
    else:
        num1=float(input("Enter the first number: "))
        num2=float(input("Enter the second number: "))
        if(opration=="+"):
            result= (num1) + (num2)
        #print(f"Addtion:{result}")
        elif(opration=="-"):
            result= (num1) - (num2)
        #print(f"subtraction:{result}")
        elif(opration=="*"):
            result= (num1) * (num2)
        #print(f"Multification:{result}")
        elif(opration=="/"):
            result= (num1) / (num2)
        #print(f"Division:{result}")
        else:
            print("Invalid operation. Please select +, -, *, or /.")
            continue

    print(f"The result of {num1} {opration} {num2} is: {result}")      
    break