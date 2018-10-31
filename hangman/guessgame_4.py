word = "hangman"
letters = [x for x in list(word)]
letters_to_guess = ["-" for x in letters]
attempts = 10
word_guessed = False
while attempts != 0 and not word_guessed:
    player_guess = str(input("\nPlease select a letter between A-Z" + "\n> ")).lower()
    if player_guess in list(word):
            indexes = [pos for pos, char in enumerate(word) if char == player_guess]
            for index in indexes:
                letters_to_guess[index] = player_guess
            print(f"yes, {player_guess} is there")
            print(letters_to_guess)
            if "-" not in letters_to_guess:
                word_guessed = True
    else:
        attempts -= 1
        print("No")
print("Congratulations you guessed it")
