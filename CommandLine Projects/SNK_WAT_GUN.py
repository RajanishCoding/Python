import random


def winner(u, c):
    if u == 's' and c == 'w' or u == 'w' and c == 'g' or u == 'g' and c == 's':
        return 1
    
    elif u == c:
        return 2
    
    else:
        return 0
    

def choose(u, c):
    if u == 's':
        print("You Choose: Snake")
    elif u == 'w':
        print("You Choose: Water")
    else:
        print("You Choose: Gun")

    if c == 's':
        print("Computer Choose: Snake")
    elif c == 'w':
        print("Computer Choose: Water")
    else:
        print("Computer Choose: Gun")



def game(n):
    # Best of 10
    w = 0
    l = 0
    t = 0

    for i in range(1, n+1):
        choice = ['s', 'w', 'g']

        print(f"\n-----Round {i}-----")
        
        u = input("\nS for Snake, W for Water, G for Gun\nEnter your Choice: ").lower()
        c = random.choice(choice)

        while u not in choice:
            print("\nWrong Input, Enter Again....")
            print(f"\n-----Round {i}-----")
            u = input("\nS for Snake, W for Water, G for Gun\nEnter your Choice: ")

        print()
        choose(u, c)
        
        k = winner(u, c)

        if k == 1:
            print(f"You Won Round {i}")
            w = w+1
        
        elif k == 0:
            print(f"You Lose Round {i}")
            l = l+1

        else:
            print(f"Tied in Round {i}")
            t = t+1
            
        print(f"\nWons :  {w}  |  Losses : {l}  |  Draws : {t}")


    print("\n-----Game Over-----\n")

    if w > l:
        print("Congratulations......\nYou Won the Match")
    
    elif w < l:
        print("You Lost the Match")

    else:
        print("Match Tied")

    print()



n = int(input("Enter Number of Rounds: "))
game(n)