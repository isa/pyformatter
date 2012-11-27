import simplejson as json

class JsonPrinter():
   options = {
      'sort_keys': False,
      'indent': 3
   }

   def __init__(self, lines, options = {}):
      self.text = ''.join(lines)
      self.options.update(options)

   def dump(self):
      code = json.loads(self.text)

      return json.dumps(code, **self.options)
