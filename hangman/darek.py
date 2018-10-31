mainword = input("Enter your word: ")
print("ok, your word is: " + mainword)


def letter_checking(letter, word):
    if letter in list(word):
        return True
    else:
        return False


def letter_occurrence(letter, word):
    count = 0
    for letterinword in list(word):
        if letterinword == letter:
            count = count + 1
    return count


attempt = 3
sum_guess_letter = 0
guess_world_letter = []
while attempt != 0 and sum_guess_letter != len(str(mainword)):
    mainletter = input("\nCheck letter - " + "\n> ")
    if not mainletter.isalpha():
        print("Must be single letter")
        attempt -= 1
        continue
    if not letter_checking(mainletter, mainword):
        print("This word doesn't include your letter")
        attempt -= 1
    if letter_checking(mainletter, mainword):
        sum_guess_letter += letter_occurrence(mainletter, mainword)
        guess_world_letter.append(mainletter)
        print(guess_world_letter)
        print("You guess the letter")
        print("This letter in the word")
        print(letter_occurrence(mainletter, mainword))
        print("times.")

        continue
while attempt != 0 and sum_guess_letter == len(mainword):
    print("You guess the world")
    exit(1)
