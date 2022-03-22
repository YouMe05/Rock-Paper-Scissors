import random
com =0 
player =0
while com<=5 and player<=5:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")


    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!","comscore :",com,"playerscore :",player)
    elif user_action == "rock":
        if computer_action == "scissors":
            player += 1
            print("Rock smashes scissors! You win!","comscore :",com,"playerscore :",player)
        else:
            com += 1
            print("Paper covers rock! You lose.","comscore :",com ,"playerscore :",player)
    elif user_action == "paper":
        if computer_action == "rock":
            player += 1
            print("Paper covers rock! You win!","comscore :",com ,"playerscore :",player)
        else:
            com += 1
            print("Scissors cuts paper! You lose.","comscore :",com ,"playerscore :",player)
    elif user_action == "scissors":
        if computer_action == "paper":
            player += 1
            print("Scissors cuts paper! You win!","comscore :",com ,"playerscore :",player)
        else:
            com += 1
            print("Rock smashes scissors! You lose.","comscore :",com ,"playerscore :",player)

    if com == 5:
        print("You Lose!!")
        break
    if player == 5:
        print("You Win!!")
        break
