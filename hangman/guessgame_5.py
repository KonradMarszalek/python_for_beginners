def letter_occurs_in_word(letter, word):
    if letter in list(word):
        return True
    else:
        return False


def letter_occurrence_count(letter, word):
    count = 0
    for each_letter in list(word):
        if each_letter == letter:
            count = count + 1
    return count


def get_letter_from_player():
    letter = input("\nCheck letter - " + "\n> ")
    while not letter.isalpha():
        print("Must be single letter")
        letter = input("\nCheck letter - " + "\n> ")
    return letter


def get_indexes(letter, word):
    indexes = []
    counter = 0
    for each_letter in word:
        if each_letter == letter:
            indexes.append(counter)
        counter += 1
    return indexes


def word_guessed(guessed_letters_sum, word):
    return guessed_letters_sum == len(word)


def run_game(attempts, word):
    print("ok, your word is: " + word)
    guessed_letters_sum = 0
    guessed_letters = []
    word_list = ["_"] * len(word)
    print(word_list)
    while attempts != 0 and not word_guessed(guessed_letters_sum, word):
        guess_letter = get_letter_from_player()
        if not letter_occurs_in_word(guess_letter, word):
            print("This word doesn't include your letter")
            attempts -= 1
        else:
            print("You guess the letter")

            current_letter_count = letter_occurrence_count(guess_letter, word)
            print(f"This letter in the word {current_letter_count} times.")

            indexes = get_indexes(guess_letter, word)
            print(f"Letter occurs in this places {indexes}.")

            guessed_letters_sum += current_letter_count
            guessed_letters.append(guess_letter)
            print(guessed_letters)
    return word_guessed(guessed_letters_sum, word)


if __name__ == "__main__":

    word_guessed = run_game(attempts=3, word=input("Enter your word: "))

    if word_guessed:
        print("You guess the word")
    else:
        print("No attempts left")
