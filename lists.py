list_letters = ['a', 'b', 'c']
list_numbers = [1, 2, 3, 10000, 3, 10000, 20]


for index in range(0, len(list_numbers)):
    print(index)
    list_numbers[index] = list_numbers[index] + 1

print(list_numbers)


