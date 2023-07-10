providedNumber = input("Please provide a number you want to check: ")
providedNumber = int(providedNumber)

numberMod = providedNumber % 2

if numberMod > 0:
    print("Your number is odd")
elif numberMod == 0:
    print("Your number is even")
else:
    print("wtf")