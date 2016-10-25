#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-03-16 16:16:14
# @Last Modified by:   anchen
# @Last Modified time: 2016-03-16 17:13:10



if __name__ == '__main__':
    from tkinter import *
    root = Tk()
    root.title('Canvas')
    canvas = Canvas(root, width = 400, height = 400,
        bg = 'yellow')
    x0 = y0 = 263
    x1 = y1 = 275
    for i in range(19):
        canvas.create_rectangle(x0, y0, x1, y1)
        x0 -= 5
        y0 -= 5
        x1 += 5
        y1 += 5

canvas.pack()
root.mainloop()