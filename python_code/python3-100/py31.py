# 星期一：Mon.=Monday
# 星期二：Tues.=Tuesday
# 星期三：Wed.=Wednesday
# 星期四：Thur.=Thursday
# 星期五：Fri.=Friday
# 星期六：Sat.=Saturday
# 星期天：Sun.=Sunday
#
#

from sys import stdin

letter = stdin.read(1)
stdin.flush()

while letter != 'Y':
    if letter == 'S':
        print('please input second letter: ')
        le = stdin.read(1)
        stdin.flush()
        if le == 'a':
            print('Saturday')
        elif le == 'u':
            print('Sunday')
        else:
            print('sec letter data err')
            break
    elif letter == 'F':
        print('Friday')
        break
    elif letter == 'M':
        print('Monday')
        break
    elif letter == 'T':
        print('please input second letter: ')
        le = stdin.read(1)
        stdin.flush()
        if le == 'u':
            print('Tuesday')
        elif le =='h':
            print('Thursday')
        else:
            print('data error')
            break
    elif letter == 'W':
        print('Wednesday')
    else:
        print('data error')
    letter = stdin.read(1)
    stdin.flush()





