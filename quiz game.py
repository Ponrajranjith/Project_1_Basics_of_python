print("Welcome to my quiz! ")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("okay! let's play")
score = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
   print("Correct!")
   score += 1
else :
    print("Incoorect!")
    
answer = input("What does GPU stands for? ")
if answer.lower() == "graphical processing unit":
   print("Correct!")
   score += 1

else :
    print("Incoorect!")

answer = input("What does RAM stands for? ")
if answer.lower() == "random accessing memory":
   print("Correct!")
   score += 1

else :
    print("Incoorect!")

answer = input("What does PSU stands for? ")
if answer.lower() == "power supply unit":
   print("Correct!")
   score += 1

else :
    print("Incoorect!")

print(f"You  got {score} questions correct")
print(f"You  got {(score/4)*100}%")

