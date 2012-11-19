from formatter.base import Printer
import simplejson as json

class JsonPrinter(Printer):
   options = {
      'sort_keys': False,
      'indent': 4
   }

   def __init__(self, text):
      self.text = text

   def dump(options = {}):
      self.options.update(options)
      code = json.loads(self.text)

      return json.dumps(code, **self.options)
