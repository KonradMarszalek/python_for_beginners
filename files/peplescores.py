with open('scores.txt') as file:
    list_from_file = file.readlines()[1:]

names = []
for line in list_from_file:
    if line == '\n':
        continue
    names.append(line.split(',')[0])
print(names)

scores = []
for line in list_from_file:
    if line == '\n':
        continue
    score = line.split(',')[1]
    score = score.rstrip('\n')
    scores.append(score)
print(scores)

maximum = scores[0]
for score in scores:
    if score > maximum:
        maximum = score

# index = [pos for pos, score in scores if score == maximum]
index = scores.index(maximum)

print(index)
print(names[index])

suma = 0
for score in scores:
    suma = suma + int(score)

average = suma / len(scores)
print(average)
