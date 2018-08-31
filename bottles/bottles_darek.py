def FitstVerse(n):
    print(n, "bottles of beer on the wall,", n, ",bottles of beer")
    print("{n} bottles of beer {n} on the wall bottles of beer".format(n=n))
    print(f"{n} bottles of beer {n} on the wall bottles of beer")

def StandardVerse(n):
    print("Take one down pass it around,", n, "bottles of beer on the wall.")
    print(n, "bottles of beer on the wall,", n, ",bottles of beer")


def TwoBottles(n):
    print("Take one down pass it around, 2 bottles of beer on the wall.")
    print("2 bottles of beer on the wall, 2 bottles of beer.")


def OneBottle(n):
    print("Take one down pass it around, 1 bottle of beer on the wall.")
    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take one down, pass it around, no more bottles of beer on the wall.")


def NoBottles(n):
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store, buy some more, 99 bottles of beer on the wall.")


for n in range(100, 0, -1):
    if n == 100:
        FitstVerse(n)
    elif n > 1:
        StandardVerse(n)
    elif n == 1:
        OneBottle(n)
    else:
        NoBottles(n)
