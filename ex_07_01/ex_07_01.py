''' Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case.
Here is the link to the file : www.py4e.com/code3/mbox-short.txt; Save it as a text file in your current folder'''
fh = open('mbox-short.txt')

for lx in fh:
    ly = lx.rstrip()
    print (ly.upper())