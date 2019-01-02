import csv

contrahents_filter = ["MLYN GOSPODARCZY", "CARREFOUR", "TESCO", "BIEDRONKA", "PIOTR I PAWEL", "LIDL"]

transaction_dates = []
contrahents = []
titles = []
amounts = []

with open("Lista_transakcji.csv") as csv_file:
    reader = csv.reader(csv_file, delimiter=';', quotechar='"')
    for row in reader:
        transaction_dates.append(row[0])
        contrahents.append(row[2])
        titles.append(row[3])
        amounts.append(row[8])

# print(transaction_dates)
# print(contrahents)
# print(titles)
# print(amounts)

indexes = []
for idx, contrahent in enumerate(contrahents):
    for contrahent_filter in contrahents_filter:
        if contrahent_filter.lower() in contrahent.lower():
            indexes.append(idx)

# print(indexes)

amount_sum = 0.0
for idx in indexes:
    if amounts[idx]:
        amount_sum += float(amounts[idx].replace(',', '.'))

print("TOTAL: ", int(amount_sum * -1))


months = ['-05-', '-06-', '-07-', '-08-', '-09-', '-10-', '-11-']

for month in months:
    month_sum = 0
    for idx in indexes:
        if amounts[idx]:
            if month in transaction_dates[idx]:
                # if month == '-10-':
                #     print(contrahents[idx])
                #     print(titles[idx])
                #     print(amounts[idx])
                month_sum += float(amounts[idx].replace(',', '.'))
    print(month, ": ", int(month_sum * -1))


