#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-03-03 16:45:11
# @Last Modified by:   anchen
# @Last Modified time: 2016-03-03 17:28:25


bonus1 = 100000 * 1
bonus2 = bonus1 + 100000 * 0.075
bonus4 = bonus2 + 200000 * 0.5
bonus6 = bonus4 + 200000 * 0.3
bonus10 = bonus6 + 400000 * 0.15


i = int(input('请输入一个利润值：'))

if i <= 100000:
    bonus = i * 0.1
elif i <= 200000:
    bonus = bonus1 + (i - 100000) * 0.075
elif i <= 400000:
    bonus = bonus2 + (i - 200000) * 0.05
elif i <= 600000:
    bonus = bonus4 + (i - 400000) * 0.03
elif i <= 1000000:
    bonus = bonus6 + (i - 600000) * 0.015
else:
    bonus = bonus10 + (i - 1000000) * 0.01
print('bonus = ', bonus)