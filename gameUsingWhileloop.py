import random

num=random.randint(1,10)

tries=0

while True:
    guess=int(input("Please guess the no. between 1 to 10: "))
    if guess==num:
        tries+=1
        print(f"you are right you guessed the number is {tries}")
        break
    elif guess>num :
        print(f"Guess low number")
        tries+=1
    else:
        print(f"guess high number")
        tries+=1