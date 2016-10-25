#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-03-16 14:17:09
# @Last Modified by:   anchen
# @Last Modified time: 2016-03-16 14:29:03

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print(x)
print(y)


print("I said: %r." % x)
print("I also said: '%s'." % y)


hilarous = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarous)

w = "This is the left side of..."
e = "a string with a right side"

print(w + e)