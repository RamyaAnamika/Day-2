num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))

opration=(input("What type of operation (+, -, *, /): "))
if(opration=="+"):
    result= (num1) + (num2)
    print(f"Addtion:{result}")
elif(opration=="-"):
    result= (num1) - (num2)
    print(f"subtraction:{result}")
elif(opration=="*"):
    result= (num1) * (num2)
    print(f"Multification:{result}")
elif(opration=="/"):
    result= (num1) / (num2)
    print(f"Division:{result}")
else:
    print("No opration")