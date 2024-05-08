import random

rand = random.randint(0, 100)

print("\nGuess the Number [0 - 100]")

i = 0
while True:
    i += 1

    print(f"\n-----Guess {i}-----")
    n = int(input("\nGuess the Number: "))
    
    if n == rand:
        print(f"Perfect Guess, its {rand}")
        print(f"You Took {i} Guesses\n")
        break

    elif n < rand:
        print("Its Lower\nEnter Higher Number....")

    else:
        print("Its Higher\nEnter Lower Number....")