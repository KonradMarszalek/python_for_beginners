my_list = [
    'My first line',
    'My second line',
    'My last line'
]

with open('new file.txt', 'w') as f:
    f.writelines(my_list)
