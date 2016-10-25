#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-03-16 16:16:14
# @Last Modified by:   anchen
# @Last Modified time: 2016-03-16 16:29:04



if __name__ == '__main__':
    a = int(input('input a number: '))
    b = a >> 4
    c = ~(~0 << 4)
    d = b & c
    print('%o\t%o' % (a, d))
