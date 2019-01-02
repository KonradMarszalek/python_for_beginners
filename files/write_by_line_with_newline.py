my_list = [
    'My first line',
    'My second line',
    'My last line'
]

my_string = '\n'.join(my_list)
with open('new file.txt', 'w') as f:
    f.write(my_string)
