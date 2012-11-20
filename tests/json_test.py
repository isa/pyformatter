from pyformatter.ext.json import JsonPrinter
from unittest import TestCase

class JsonPrinterTest(TestCase):
   def test_dump_should_have_new_lines_when_only_one_pair(self):
      code = '{"key": "value"}'
      json_printer = JsonPrinter(code)

      actual = json_printer.dump()
      self.assertEqual(2, actual.count('\n'))

   def test_dump_should_have_new_lines_when_more_than_one_pair(self):
      code = '{"key1": "value1", "key2": "value2"}'
      json_printer = JsonPrinter(code)

      actual = json_printer.dump()
      self.assertEqual(3, actual.count('\n'))

   def test_dump_should_indent_with_three_spaces_when_only_one_pair(self):
      three_space = "   "
      code = '{"key": "value"}'
      expected_number_of_indentation = 1
      json_printer = JsonPrinter(code)

      actual = json_printer.dump()
      self.assertTrue(actual.count(three_space) is expected_number_of_indentation)

   def test_dump_should_indent_with_four_spaces_when_options_passed(self):
      four_space = "    "
      code = '{"key": "value"}'
      options = {'indent': 4}
      expected_number_of_indentation = 1
      json_printer = JsonPrinter(code)

      actual = json_printer.dump(options)
      self.assertTrue(actual.count(four_space) is expected_number_of_indentation)

   def test_dump_should_indent_with_three_spaces_when_more_than_one_pair(self):
      three_space = "   "
      code = '{"key1": "value1", "key2": "value2"}'
      expected_number_of_indentation = 2
      json_printer = JsonPrinter(code)

      actual = json_printer.dump()
      self.assertTrue(actual.count(three_space) is expected_number_of_indentation)

   def test_dump_should_indent_array_items_with_three_spaces(self):
      three_space = "   "
      code = '{"key": ["value1", "value2"]}'
      expected_number_of_indentation = 6
      json_printer = JsonPrinter(code)

      actual = json_printer.dump()
      self.assertTrue(actual.count(three_space) is expected_number_of_indentation)

   def test_dump_should_sort_keys_when_options_passed(self):
      options = {'sort_keys': True}
      code = '{"zzz": "value1", "aaa": "value2"}'
      first_key_position = len('{\n   "') + 1
      json_printer = JsonPrinter(code)

      actual = json_printer.dump(options)
      self.assertTrue(actual.find('aaa') is first_key_position)
