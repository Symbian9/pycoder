#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-03-03 16:45:11
# @Last Modified by:   anchen
# @Last Modified time: 2016-03-07 13:43:32


# year = int(input('year: '))
# month = int(input('month: '))
# day = int(input('day: '))


# months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
# if 0 <= month <= 12:
#     sum = months[month - 1]
# else:
#     print('data error')

# sum += day
# leap = 0

# if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
#     leap = 1
# if (leap == 1) and month > 2:
#     sum +=1
# print("it s the %dth day. " % sum)


# 标准库 datetime 定义了4个主要的对象，每个对象有很多方法：
# date 处理年、月、日
# time 处理时、分、秒
# datetime 处理日期和时间同时出现的情况
# timedelta 处理日期和/或者时间间隔

import datetime

year = int(input('year: '))
month = int(input('month: '))
day = int(input('day: '))

days = datetime.date(year, month, day) - datetime.date(year, 1, 1) + \
datetime.timedelta(days=1)


print('=' * 20)
print('输出方式一：旧格式，c语言风格。')
print('这一天是这一年的第 %d 天。' % days.days)        # 旧格式
# print('这一天是这一年的第', days.days, '天。')
print('=' * 20)
print('输出方式二：字符串str.format()方法')
print('这一天是这一年的第 {} 天。'.format(days.days))


