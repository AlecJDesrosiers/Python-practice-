import random

print("Rock.....")
print("Paper.....")
print("Scissor.....")

player = input("Player 1, make your move: ").lower()
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
    else:
        print("computer wins!")
elif player == "paper":
    if computer == "rock":
        print ("player wins!")
    elif computer == "scissor":
        print("computer wins!")
elif player == "scissors":
    if computer == "rock":
        print("computer wins!")
    elif computer == "rock":
        print ("computer wins")
else: 
    print("something went wrong")
