from os import path
from pyformatter.ext.json import JsonPrinter

class Printer():
   def __init__(self, file_name):
      self.file_name = file_name
      self.text = open(file_name, 'r').read() if (path.isfile(file_name)) else ''

   def pretty_print(self, options = {}):
      ext = path.splitext(self.file_name)[1]
      if ext == '.json':
         return JsonPrinter(self.text).dump(options)

      return self.text
