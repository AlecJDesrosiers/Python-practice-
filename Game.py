import random
player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
    print(f"player Score: {player_wins} Computer score: {computer_wins}")
    print("Rock.....")
    print("Paper.....")
    print("Scissor.....")

    player = input("Player 1, make your move: ").lower()
    if player == "quit" or player == "q":
        break
    rand_num = random.randint(0,2)
    if rand_num == 0: 
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    elif rand_num == 2:
        computer = "scissor"
    print(f"computer plays {computer} ")

    if  player == computer:
        print("Its's a tie")
    elif player == "rock":
        if computer == "scissors":
            print ("player wins!")
            player_wins += 1
        else:
            print("computer wins!")
            computer_wins += 1 
    elif player == "paper":
        if computer == "rock":
            print ("player wins!")
            player_wins += 1
        elif computer == "scissor":
            print("computer wins!")
            computer_wins += 1
    elif player == "scissors":
        if computer == "rock":
            print("computer wins!")
            computer_wins += 1
        elif computer == "rock":
            print ("computer wins")
            computer_wins += 1
    else: 
        print("something went wrong")
if player_wins > computer_wins:
    print("GRATZ!")
else:
    print("YOU SUCK!")
print((f"Final scores... Player: {player_wins} Computer: {computer_wins}"))