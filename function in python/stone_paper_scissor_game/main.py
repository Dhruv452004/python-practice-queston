import random
choices = ["stone", "paper", "scissor"]

# ek function bnaya game naam jisme game ka logic likha h
def game():

    computer_wins = 0
    you_wins = 0
    draws = 0
    attempts = 5

# User se input lene ke liye while loop, valid input tak loop chalega
# .lower() agr koi Stone STONE ese type krega tho ye use small mein kr dega stone
    while attempts > 0:
         # computer isme se koi bhi random value choose krega
         computer = random.choice(choices)

         userInput = input("type stone or paper or scissor: ").lower()

         if userInput not in choices: 
        # agr userInput yourChoice dict nahi hoga tho error ko handle krne k liye ye print hoga
            print("Invalid input! Please type 'stone', 'paper', or 'scissor'.")
            continue
             
         you = userInput
         print(f"You chose: {you}, Computer chose: {computer}")

         if(computer == you):  # agr computer and you dono same hue tho draw hoga
          print("game ho gya draw")
          draws += 1

# mene ye 3 condition di agr isme se koi bhi match hoti h tho user har jayga
         elif(computer == "stone" and you == "scissor") or\
            (computer == "paper" and you == "stone") or\
            (computer == "scissor" and you == "paper"):
            print("Aap haar gaye")
            computer_wins += 1

# agr upr diye gye conditon match nahi hoti tho user jeetega
         else:
            print("aap jeet gaye")
            you_wins += 1

         attempts -= 1
         print(f"Remaining attempts: {attempts}")

    print("\nGame Over!")
    print(f"Final Scores:")
    print(f"You Wins: {you_wins}")
    print(f"Computer Wins: {computer_wins}")
    print(f"Draws: {draws}")



# game ko dubara khelne k liye 
while True:
    game() #fucntion ko call kra
    play_again = input("Kya aap dobara khelna chahenge? (y/n): ").lower()
    if(play_again == "n"):
        print(" nahi khelna ")
        break


