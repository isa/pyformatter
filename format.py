#!/usr/bin/env python

import sys

from pyformatter.base import Printer
from pygments.lexers import guess_lexer, get_lexer_for_filename
from pygments import highlight
from pygments.formatters import TerminalFormatter

if __name__ == '__main__':
   if len(sys.argv) < 2:
      sys.exit("You need to provide a file to format!")

   file_name = sys.argv[1]
   printer = Printer(file_name)
   lexer = get_lexer_for_filename(file_name)
   print highlight(printer.pretty_print(), lexer, TerminalFormatter())