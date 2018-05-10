def say_what(word):
    if not word:
        return "WHAT???"
    if word == "what":
        return "WHAT WHAT WHAT???"
    return word + ", what?"


print(say_what('Ewa i Darek'))
print(say_what('Konrad'))

