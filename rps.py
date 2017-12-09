from random import randint


def rock_paper_scissors():
    player = input('Rock (r/R) , Paper (p/P) or Scissor (s/S)? ')

    # a random number is generated (1/2/3)
    c = randint(1, 3)

    if player == 'r' or player == 'R':
        print("O vs", end=" ")
        f = 0
        p = 1
    elif player == 'p' or player == 'P':
        print("____ vs", end=" ")
        f = 0
        p = 2
    elif player == 's' or player == 'S':
        print(">8 vs", end=" ")
        f = 0
        p = 3
    # for invalid choice
    else:
        f = 1

    # if valid choice
    if f == 0:
        if c == 1:
            print("O")
        elif c == 2:
            print("____")
        else:
            print(">8")

    # if valid choice
    if f != 1:
        if p == c:
            print("DRAW!!!")
        elif p == 1 and c == 3:
            print("Player won!!!")
        elif p == 1 and c == 2:
            print("Computer won!!!")
        elif p == 2 and c == 1:
            print("Player won!!!")
        elif p == 2 and c == 3:
            print("Computer won!!!")
        elif p == 3 and c == 2:
            print("Player won!!!")
        elif p == 3 and c == 1:
            print("Computer won!!!")
    # if invalid choice
    else:
        print("Invalid Choice!!!")


rock_paper_scissors()