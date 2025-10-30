import random

# Computer generates a random number between 1 and 100
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
secret_number = random.randint(num1, num2)

print(f"Guess the number between {num1} and {num2}!")

while True:
    guess = int(input("Your guess: "))
    
    if guess < secret_number:
        print(f"Too low!")
    elif guess > secret_number:
        print(f"Too high!")
    else:
        print("Congratulations! You guessed it!")
        print(f"The secret number is:{secret_number}")
        break
