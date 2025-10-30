import random
length=int(input("what is your password length: "))
def generate_password(length, use_numbers=True, use_symbols=True):

    lowercase_chars = "abcdefghijklmnopqrstuvwxyz"
    uppercase_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

    char_pool = lowercase_chars + uppercase_chars  

    if use_numbers: 
        char_pool += numbers
    if use_symbols:
        char_pool += symbols

    password = ""
    for i in range(length):
        password += random.choice(char_pool)
    return password
print("Your password:", generate_password(length, use_numbers=False, use_symbols=False))