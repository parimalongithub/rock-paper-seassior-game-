import random


def game():
    a = input("please choose between Rock[R],Paper[P]and Seassior[S]")
    rannum = random.randint(1, 3)
    if rannum == 1:
        x = "R"
    elif rannum == 2:
        x = "P"
    elif rannum == 3:
        x = "S"
    print("computer chooses", x)
    if x == a:
        return None
    elif x == "S" and a == "R":
        return True
    elif x == "S" and a == "P":
        return False
    elif x == "R" and a == "P":
        return True
    elif x == "R" and a == "S":
        return False
    elif x == "P" and a == "S":
        return True
    elif x == "P" and a == "R":
        return False


b = game()

if b is None:
    print("the game is tie")
elif b:
    print("you win the game!")
elif not b:
    print("you lose the game")
     

    


    

    
    

    





















