NUMBER=21
attempts=0
while True:
    guess =int(input("ENTER YOUR GUESS NUMBER:"))
    attempts+=1
    if guess>NUMBER:
        print("HIGHER")
    elif guess<NUMBER:
        print("LOWER")
    else:
        print("CORRECT YOU WON!")
        print("ATTEMPTS TAKEN:",attempts)
        break