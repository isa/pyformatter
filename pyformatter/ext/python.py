import tokenize

# Code is heavily adapting 'reindent.py' by Tim Peters
# Thanks to him to make his code public

class PythonPrinter():
   options = {
      'indent': 3
   }

   def __init__(self, lines, options = {}):
      self.options.update(options)
      self.find_stmt = 1  # next token begins a fresh stmt?
      self.lines = [None]
      self.lines.extend(lines)
      self.index = 1  # index into self.lines of next line
      self.indent_level = 0
      self.stats = []

   def remove_trailing_empty_lines(self):
      lines = self.lines
      while lines and lines[-1] == "\n":
         lines.pop()
      return lines

   def dump(self):
      tokenize.tokenize(self.get_line, self.token_eater)
      lines = self.remove_trailing_empty_lines()
      stats = self.stats
      stats.append((len(lines), 0))
      # Map count of leading spaces to # we want.
      have2want = {}
      # Program after transformation.
      after = self.after = []
      # Copy over initial empty lines -- there's nothing to do until
      # we see a line with *something* on it.
      i = stats[0][0]
      after.extend(lines[1:i])
      for i in range(len(stats)-1):
         thisstmt, thislevel = stats[i]
         nextstmt = stats[i+1][0]
         have = self.get_leading_spaces(lines[thisstmt])
         want = thislevel * self.options['indent']
         if want < 0:
            # A comment line.
            if have:
               # An indented comment line.  If we saw the same
               # indentation before, reuse what it most recently
               # mapped to.
               want = have2want.get(have, -1)
               if want < 0:
                  # Then it probably belongs to the next real stmt.
                  for j in xrange(i+1, len(stats)-1):
                     jline, jlevel = stats[j]
                     if jlevel >= 0:
                        if have == self.get_leading_spaces(lines[jline]):
                           want = jlevel * self.options['indent']
                        break

               if want < 0:         # Maybe it's a hanging
                                    # comment like this one,
                  # in which case we should shift it like its base
                  # line got shifted.
                  for j in xrange(i-1, -1, -1):
                     jline, jlevel = stats[j]
                     if jlevel >= 0:
                        want = have + self.get_leading_spaces(after[jline-1]) - \
                              self.get_leading_spaces(lines[jline])
                        break

               if want < 0:
                  # Still no luck -- leave it alone.
                  want = have
            else:
               want = 0
         assert want >= 0
         have2want[have] = want
         diff = want - have
         if diff == 0 or have == 0:
            after.extend(lines[thisstmt:nextstmt])
         else:
            for line in lines[thisstmt:nextstmt]:
               if diff > 0:
                  if line == "\n":
                     after.append(line)
                  else:
                     after.append(" " * diff + line)
               else:
                  remove = min(self.get_leading_spaces(line), -diff)
                  after.append(line[remove:])
      return ''.join(self.after)

   # Count number of leading blanks.
   def get_leading_spaces(self, line):
      i, n = 0, len(line)
      while i < n and line[i] == " ":
         i += 1
      return i

   def get_line(self):
      if self.index >= len(self.lines):
         line = ""
      else:
         line = self.lines[self.index]
         self.index += 1

      return line

   def token_eater(self, type, token, (sline, scol), end, line, INDENT=tokenize.INDENT, DEDENT=tokenize.DEDENT, NEWLINE=tokenize.NEWLINE, COMMENT=tokenize.COMMENT, NL=tokenize.NL):

      if type == NEWLINE:
         # A program statement, or ENDMARKER, will eventually follow,
         # after some (possibly empty) run of tokens of the form
         #     (NL | COMMENT)* (INDENT | DEDENT+)?
         self.find_stmt = 1

      elif type == INDENT:
         self.find_stmt = 1
         self.indent_level += 1

      elif type == DEDENT:
         self.find_stmt = 1
         self.indent_level -= 1

      elif type == COMMENT:
         if self.find_stmt:
            self.stats.append((sline, -1))
            # but we're still looking for a new stmt, so leave
            # find_stmt alone

      elif type == NL:
         pass

      elif self.find_stmt:
         # This is the first "real token" following a NEWLINE, so it
         # must be the first token of the next program statement, or an
         # ENDMARKER.
         self.find_stmt = 0
         if line:   # not endmarker
            self.stats.append((sline, self.indent_level))
