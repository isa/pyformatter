   def check(file):
             if os.path.isdir(file) and not os.path.islink(file):
                 if verbose:
                           print "listing directory", file
                 names = os.listdir(file)
                 for name in names:
                     fullname = os.path.join(file, name)
                     if ((recurse and os.path.isdir(fullname) and
                          not os.path.islink(fullname) and
                          not os.path.split(fullname)[1].startswith("."))
                         or name.lower().endswith(".py")):
                               check(fullname)
                 return
