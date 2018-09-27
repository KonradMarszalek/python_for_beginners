from pprint import pprint

lyrics = """
SNÓW DOBRYCH ŻYCZENIA
Otwieram złotą furtkę snu:
Cóż za tą furtką? – Białe jaśminy

Księżniczka z koszykiem zbiera jeżyny
To tam, to tu.
Jeżyn są grona czarne jak noce,
Niebieskie kwiaty stoją przy drodze,
Lis ścieżkę omiata płomienną kitą,
Nad trawą bocian stoi obmytą
Rosą czy deszczem? Ja sprawę tą
Zostawiam snom, co wam się śnią

Otwieram złotą furtkę snu:
Cóż za tą furtką? – Potężny zamek,
Zamknięty na tysiąc tajemnych klamek,
Przeciwko złu.
Straże was strzegą na strzelistych wieżach3
,
Konie dyszące w żelaznych pancerzach,
Książę choć dobry dzieciom dobrotliwy,
Któremu służą potworki i dziwy:
Jakie? pytacie. Ja sprawę tą
Zostawiam snom, co wam się śnią
"""

wordcount = {}


def word_count(text):
    for word in text.split():
        word = word.lower()
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    return wordcount


pprint(word_count(lyrics))

# https://exercism.io/tracks/python/exercises
