#!/usr/bin/env python3
import os
import sys

def getUnionOfKmerFreq(fileName, fileName2, fileToWrite):
    f = open(fileName, 'r')
    f2 = open(fileName2, 'r')
    out_f = open(fileToWrite,'a')

    line = f.readline()
    line2 = f2.readline()
    while line and line2:

        key = line.split(" ",1)[0]
        vals = int(line.split(" ",1)[1])

        key2 = line2.split(" ",1)[0]
        vals2 = int(line2.split(" ",1)[1])

        if(key==key2):
            out_f.write("%s %s\n" % (vals,vals2))
            line = f.readline()
            line2 = f2.readline()

        if(key!=key2 and key < key2):
            out_f.write("%s %s\n" % (vals,0))
            line = f.readline()

        if(key!=key2 and key2 < key):
            out_f.write("%s %s\n" % (0,vals2))
            line2 = f2.readline()

    if line2 == '' and line != '':
        while line:
            key = line.split(" ",1)[0]
            vals = int(line.split(" ",1)[1])
            out_f.write("%s %s\n" % (vals,0))
            line = f.readline()

    elif line == '' and line2 != '':
        while line2:
            key2 = line2.split(" ",1)[0]
            vals2 = int(line2.split(" ",1)[1])
            out_f.write("%s %s\n" % (0,vals2))
            line2 = f2.readline()

    f.close()
    f2.close()
    out_f.close()

def main():
    fileName = sys.argv[1] #sample 1
    fileName2 = sys.argv[2] #sample 2
    fileToWrite = sys.argv[3] #file to store union of kmers in sample1 and sample2 

    getUnionOfKmerFreq(fileName, fileName2, fileToWrite)

if __name__ == '__main__':
    main()
