# Python's list comprehensions are awesome.

# vals = [expression
#         for value in collection
#         if condition]

# This is equivalent to:

# vals = []
# for value in collection:
#     if condition:
#         vals.append(expression)

# Example:

# even_squares = [
#                 for x in range(0, 10)
#                 if not x % 2]
# print(even_squares)

even_squares = []

for x in range(0, 10):
    if not x % 2:
        even_squares.append(x * x)
print(even_squares)




