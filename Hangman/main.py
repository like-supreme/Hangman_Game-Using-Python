import random
from ascii_logos import stages
from logo import logo
from words import word_list

def start_game():
    print(logo)
    chosen_word = random.choice(word_list)
    print(chosen_word)
    lives = 6
    stage_index = 0
    stored_words = set()
    placeholder = []
    for number in range(len(chosen_word)):
        number = "_"
        placeholder.append(number) 
    print(*placeholder) # _ _ _ _ _ etc
    print(stages[0])
    while True:
        guess = input("Guess a letter: ").lower()
        if guess in stored_words:
            print("You already try this letter. Try something else :)...")
            continue
        else:
            stored_words.add(guess)
        if guess == "stop":
            break
        if guess not in chosen_word:
            lives -= 1 
            stage_index += 1
            print(stages[stage_index])     
            print(f"current_live is: {lives}")  
            
            if lives == 0:
                print("You loose")
                print(stages[6])
                break
            else:
                continue    
        if "_" not in placeholder:
            print(*placeholder)
            print("You Won")
            break
        else:
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:    
                    placeholder[i] = guess
                    
                    print(*placeholder)

while True:
    start_game()
    start_again = input("Would you like to play again y/n?...")
    if start_again != "y":
        print("Goodbye")
        break