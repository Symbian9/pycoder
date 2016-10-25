#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-03-11 14:48:32
# @Last Modified by:   anchen
# @Last Modified time: 2016-03-11 14:51:01


def hello_world():
    print('hello world')

def three_hellos():
    for i in range(3):
        hello_world()


if __name__ == '__main__':
    three_hellos()