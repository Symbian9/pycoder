
def palin(n):
    nextx = 0
    if n <= 1:
        nextx = input('input a char: ')
        print()
        print(nextx)
    else:
        nextx = input('input a char: ')
        palin(n - 1)
        print(nextx)


palin(5)