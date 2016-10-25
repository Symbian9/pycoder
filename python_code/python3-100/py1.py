#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-03-03 16:45:11
# @Last Modified by:   anchen
# @Last Modified time: 2016-03-03 17:00:24


for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != k ) and (i != j ) and (j != k ):
#                print(i, j, k)
                print(str(i) + str(j) + str(k))