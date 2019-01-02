import csv

lista = []
scores = []
with open("scores.zosia") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        lista.append(row['Name'])
        scores.append(row['Score'])



print(lista)
print(scores)






