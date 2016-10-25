#import string

s = input('input a strng: ')

letters = space = digit = other = 0

for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        other += 1
print('char = %d, space = %d, digit = %d, other = %d' % (letters, space, digit,other))