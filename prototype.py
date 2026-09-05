import random
import time

is_password_valid = True

while is_password_valid:
    print("Choose a password length between 8 and 100.")
    passwordlength = int(input())
    if passwordlength < 8 or passwordlength > 100:
        print("Enter the correct number of characters for the password.")
        break
    else:
        text = "Generating : ▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮"
        for char in text:
            print(char, end = "", flush=True)
            time.sleep(0.1)
    print()

    english_letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    safe_symbols = [
        '!', '@', '#', '$', '%', '^', '&', '*', 
        '(', ')', '_', '-', '+', '=', '[', ']', 
        '{', '}', ';', ':', ',', '.', '?'
    ]

    combined = english_letters + numbers + safe_symbols

    password = ""

    for _ in range(passwordlength):
        password += f"{random.choice(combined)}"
    print(f"Here is your password: {password}")
    break
