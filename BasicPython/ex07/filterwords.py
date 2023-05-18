from sys import argv
import re
if (len(argv) == 1) or (len(argv) > 3) or (len(argv) < 3):
  print("ERROR")
elif (argv[1].isnumeric()) or (not argv[2].isnumeric()):
  print("ERROR")
else:
  word = argv[1]
  num = int(argv[2])
  word = re.sub(r'[^\w\s]', ' ', word)
  word = word.split()
  wordsInRange = [i for i in word if len(i) > num]
  print(wordsInRange)