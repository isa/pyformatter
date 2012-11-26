from os import path
from pyformatter.ext.json import JsonPrinter
from pyformatter.ext.python import PythonPrinter

class Printer():
   def __init__(self, file_name):
      self.file_name = file_name
      lines = open(file_name, 'r').readlines() if (path.isfile(file_name)) else ''
      self.text = [line.rstrip().expandtabs() + '\n' for line in lines]

   def pretty_print(self, options = {}):
      ext = path.splitext(self.file_name)[1]
      if ext == '.json':
         return JsonPrinter(self.text).dump(options)
      elif ext == '.py':
         return PythonPrinter(self.text).dump(options)

      return self.text
