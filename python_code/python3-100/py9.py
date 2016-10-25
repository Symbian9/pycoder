
import sys
a = 219

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            sys.stdout.write(chr(a))
            sys.stdout.write(chr(a))
        else:
            sys.stdout.write(' ' * 2)
    print(' ')
