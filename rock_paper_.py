import random 

user_win = 0 
computer_win = 0

option = ["rock","paper","scissors"]

while True:
    user_input = input("Type rock/paper/scissors or q to quit").lower()
    if user_input == "q":
        break
        if user_input not in option:
            continue

    random_number = random.randint(0,2)

    computer_pick = option[random_number]
    print("computer picked ",computer_pick + ".")

    if user_input == "rock" and computer_pick =="scissors":
        print("you won!")
        user_win += 1

    elif user_input == "paper" and computer_pick =="rock":
        print("you won!")
        user_win += 1

    elif user_input == "scissors" and computer_pick =="paper":
        print("you won!")
        user_win += 1

    else:
        print("You lost!")
        computer_win +=1

    
print("You won ",user_win,"times")
print("Computer won ",computer_win,"times")
print("Goodbye!")

