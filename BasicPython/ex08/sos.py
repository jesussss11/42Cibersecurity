print("\033[1;32m")
import re
from sys import argv
import sys

morse = {
    " ":	"/",
	"A":	".-",
	"B":	"-...",
	"C":	"-.-.",
	"D":	"-..",
	"E":	".",
	"F":	"..-.",
	"G":	"--.",
	"H":	"....",
	"I":	"..",
	"J":	".---",
	"K":	"-.-",
	"L":	".-..",
	"M":	"--",
	"N":	"-.",
	"O":	"---",
	"P":	".--.",
	"Q":	"--.-",
	"R":	".-.",
	"S":	"...",
	"T":	"-",
	"U":	"..-",
	"V":	"...-",
	"W":	".--",
	"X":	"-..-",
	"Y":	"-.--",
	"Z":	"--..",
	"0":	"-----",
	"1":	".----",
	"2":	"..---",
	"3":	"...--",
	"4":	"....-",
	"5":	".....",
	"6":	"-....",
	"7":	"--...",
	"8":	"---..",
	"9":	"----."
}

text = len(argv)
if text >= 2:
	str = ' '.join(argv[1:])
    #regex = any alphabetic or numeric character
	if re.search(r'[^a-zA-Z\d\s]', str):
		sys.exit('Error')
	for chr in str:
		print(morse[chr.upper()],end=' ')
	print() #Remove percentage