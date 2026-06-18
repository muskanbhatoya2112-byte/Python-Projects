import random

class WeakPassword(Exception):
    pass

pwd = ""
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789@#"
for i in range(8):
    pwd += random.choice(chars)

print("Generated Password:", pwd)

try:
    p = input("Enter Password: ")

    if len(p) < 8:
        raise WeakPassword("Password too short")

    print("Valid Password")

except WeakPassword as e:
    print(e)