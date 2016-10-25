#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-03-24 14:53:27
# @Last Modified by:   anchen
# @Last Modified time: 2016-03-24 15:03:05


import sys, re
from util import *

print('<html><head><title>...</title><body>')


title = True
for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')


print('</body></html>')
