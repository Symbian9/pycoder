#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-03-16 16:16:14
# @Last Modified by:   anchen
# @Last Modified time: 2016-03-16 16:21:52



TRUE = 1
FLASE = 0

def SQ(x):
    return x * x

print('Program will stop if input value less than 50.')


again = 1
while again:
    num = int(input('Please input number'))
    print('The square for this number is %d' % (SQ(num)))
    if num >= 50:
        again = TRUE
    else:
        again = FLASE