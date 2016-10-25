#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-03-16 16:16:14
# @Last Modified by:   anchen
# @Last Modified time: 2016-03-16 16:58:47



if __name__ == '__main__':
    from tkinter import *

canvas = Canvas(width = 800, height = 600, bg = 'yellow')
canvas.pack(expand = YES, fill = BOTH)
k = 1
j = 1
for i in range(0, 26):
    canvas.create_oval(301 - k, 250 - k, 310 + k, 250 + k, width = 1)
    k += j
    j += 0.3

mainloop()