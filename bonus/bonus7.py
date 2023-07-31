# example of list comprehensions. Want to replace . with a - as well

filenames = ["1.doc", "1.report", "1.presentation"]

filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]

print(filenames)
