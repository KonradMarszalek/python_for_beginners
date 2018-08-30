i = 1  # Try without it


def foo():
    i = 5
    print(i, 'in foo()')


print(i, 'global')

foo()
