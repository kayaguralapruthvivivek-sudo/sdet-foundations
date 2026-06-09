num = 18
guess = int(input("what's your guess for number"))
while guess != num:
    if guess < num:
        print("Too low")
    else:
        print("Too High")
    guess = int(input("what's your guess for number"))
print("You're correct")


