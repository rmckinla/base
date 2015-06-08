import os

def run(**args):
  print "[-] Info"
  files = os.listdir(".")
  return str(files)
