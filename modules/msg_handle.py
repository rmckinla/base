import os

def msg_handle(**args):
  print "[-] Info"
  files = os.listdir(".")
  return str(files)
