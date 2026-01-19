import random
import string

try:
    length = int(input("enter the length of the password:"))
    count = int(input("enter the number of passwords to generte:"))

    if length < 5:
        print("password length should be at least 5")
    elif count < 1:
        print("number of the passwords should be at least 1")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        for i in range(count):
            password = ''.join(random.choice(characters) for i in range(length))
            print("generated password is:", password)
except ValueError:
    print("invalid input. please enter valid integers.")
except Exception as e:
    print(f"an unexpected error occurred: {e}")