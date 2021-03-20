#!/usr/bin/env python3
import os
import sys

def getIntersectOfKmers(fileName, fileName2, fileToWrite):
    f = open(fileName)
    f2 = open(fileName2)
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
            line = f.readline()

        if(key!=key2 and key2 < key):
            line2 = f2.readline()

    f.close()
    f2.close()
    out_f.close()

def main():
    fileName = sys.argv[1] #sample 1
    fileName2 = sys.argv[2] #sample 2
    fileToWrite = sys.argv[3] #file to store intersection of kmers in sample1 and sample2 

    getIntersectOfKmers(fileName, fileName2, fileToWrite)

if __name__ == '__main__':
    main()
