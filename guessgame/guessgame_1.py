word = "hangman"
attempts = 10
while attempts != 0:
    player_guess = str(input("\nPlease select a letter between A-Z" + "\n> ")).lower()
    if player_guess in list(word):
            print(f"yes, {player_guess} is there")
    else:
        attempts -= 1
        print("No")
