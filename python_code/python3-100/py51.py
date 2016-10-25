#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-03-16 16:16:14
# @Last Modified by:   anchen
# @Last Modified time: 2016-03-16 16:25:52



if __name__ == '__main__':
    a = 0x077
    b = a & 3
    print('a & b = %d' % b)
    b &= 7
    print('a & b = %d' % b)