#Hangman Game
import random
import hangman_stages,hangman_word_list

print(hangman_stages.logo)
choice = random.choice(hangman_word_list.word_list).lower()
print(f"Pssst, the solution is {choice}")


#Initializing variables
display=[ "_" for i in range(len(choice))]
lives=6

while (lives > 0):
    guess = input("Guess a letter: ").lower()
    for position in range(len(choice)):
        if  choice[position] == guess:
            display[position] = guess
    
    print(" ".join(display))
    if guess not in display:
        lives-=1
        print(hangman_stages.stages[lives])
    else:
        
        if "_" not in display:
            print("You Win!!")
            break
        else:
            print(hangman_stages.stages[lives])
            


    

