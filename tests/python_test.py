from pyformatter.ext.python import PythonPrinter
from unittest import TestCase

class PythonPrinterTest(TestCase):

   def test_dump_should_indent_with_three_spaces(self):
      three_space = "   "
      lines = ['def method():', ' a_statement']
      expected_number_of_indentation = 1
      python_printer = PythonPrinter(lines)

      actual = python_printer.dump()
      self.assertTrue(actual.count(three_space) is expected_number_of_indentation)

   def test_dump_should_indent_with_four_spaces(self):
      four_space = "   "
      lines = ['def method():', ' a_statement']
      expected_number_of_indentation = 1
      options = { 'indent': 4 }
      python_printer = PythonPrinter(lines, options)

      actual = python_printer.dump()
      self.assertTrue(actual.count(four_space) is expected_number_of_indentation)

