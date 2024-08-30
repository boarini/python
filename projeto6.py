import random
word_list =["aardvark" , "babbon", "camel"]

chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)

placeholder = ""
game_over = False
correct_letters = []
player_lives = 6

while not game_over:
    for position in range(word_lenght):
        placeholder += "_"

    guess = str.lower(input("Guess a letter: "))

    display =""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    if guess not in correct_letters:
        player_lives -= 1
        print(f"Wrong guess! You have {player_lives} lives left.")
        if player_lives == 0:
            game_over = True
            print("You lose.")
            break
    print(display)

    if "_" not in display:
        game_over = True
        print("You win.")
    