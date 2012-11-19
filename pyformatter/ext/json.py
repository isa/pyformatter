import simplejson as json

class JsonPrinter():
   options = {
      'sort_keys': False,
      'indent': 4
   }

   def __init__(self, text):
      self.text = text

   def dump(self, options = {}):
      self.options.update(options)
      code = json.loads(self.text)

      return json.dumps(code, **self.options)
