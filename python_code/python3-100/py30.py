
x = input('input a number: ')

for i in range(len(x) // 2):
    if x[i] != x[-i - 1]:
        print('this number is not a huiwen.')
        break
    else:
        print('this number is a huiwen.')
        break

