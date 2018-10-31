word = "hangman"
letters = [x for x in list(word)]
letters_to_guess = ["-" for x in letters]
attempts = 10
word_guessed = False
while attempts != 0 or word_guessed == True:
    player_guess = str(input("\nPlease select a letter between A-Z" + "\n> ")).lower()
    if player_guess in list(word):
        print(f"yes, {player_guess} is there")
        index = word.index(player_guess)
        letters_to_guess[index] = player_guess
        print(letters_to_guess)
        if "-" not in letters_to_guess:
            word_guessed = True
    else:
        attempts -= 1
        print("No")
print("Congratulations you guessed it")
