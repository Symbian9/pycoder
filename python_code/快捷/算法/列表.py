# nrows 为行数
# ncols 为列数
def timesTable():
    for row in range(1, 5):
      for col in range(1, 6):
         print "%3d "% (row * col),
      print
timesTable()
      