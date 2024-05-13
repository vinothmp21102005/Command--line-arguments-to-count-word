# program to count the words from the command line
# Name : VINOTH M p
# Reg No :  212223240182


import sys
count = 0
with open(sys.argv[1],'r') as f:
    for i in f:
        word = i.split()
        count += len(word)
print("word count in file =" , count)