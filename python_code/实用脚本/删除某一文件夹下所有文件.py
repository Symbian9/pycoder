import sys
import os
def DeleteFile(dirName):
  if dirName == "" or not os.path.exists(dirName):
    print "%s is a null string or not exist, input param error! " % dirName
    return
  try:
    if os.path.isfile(dirName):
      os.remove(dirName)
    else:
      for file in os.listdir(dirName):
        DeleteFile(os.path.join(dirName, file))
      os.rmdir(dirName)
    print "deleted the file/dir :%s" % dirName
  except:
    print "there is a Error in deleting files/dires: %s" % dirName
    print sys.exc_info()
def DeleteFilesInDir(dirName):
  if os.path.isdir(dirName) :
    for file in os.listdir(dirName):
      DeleteFile(os.path.join(dirName, file))
  else:
    print "%s is not a directory" % dirName
if __name__ == "__main__":
  DeleteFilesInDir(r"d:\temp")
  DeleteFilesInDir(r"d:\nulldir") 
  DeleteFilesInDir(r"d:\afile.txt")
  DeleteFilesInDir(r"d:\notexist.txt")