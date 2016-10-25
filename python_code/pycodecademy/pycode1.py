#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-03-15 17:13:57
# @Last Modified by:   anchen
# @Last Modified time: 2016-03-15 17:22:05


class Fruit(object):
    'A class that makes various tasty fruits.'
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print("I'm a %s %s and I taste %s" % (self.color, self.name, self.flavor))

    def is_edible(self):
        if not self.poisonous:
            print("Yep! I'm edible")
        else:
            print("Don't eat me! I am super poisonous.")

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()