#!/usr/bin/env python3
import os
import sys
import glob
import subprocess
from os.path import basename
from subprocess import call


def countFrequencies(names,kvalue):

    for i in range(0,len(names),1):

        fileOne = names[i]

        subscriptIndex = fileOne.split(".")

        fileNameOut = "%s.jf" % (subscriptIndex[0])

        subprocess.call("/bin/bash -c \"jellyfish count %s -m %d -s 100M -t 50 -C --disk -o %s\"" % (fileOne, kvalue, fileNameOut), shell=True)

        dotIdx = fileNameOut.split(".")

        fileName = dotIdx[0]

        fileNameOutFA = "%s_%smer_profile.fa" % (fileName, kvalue)

        subprocess.call("jellyfish dump %s > %s -c" % (fileNameOut, fileNameOutFA), shell=True)

        subprocess.call("find . -type f -iname \*.jf -delete", shell=True)


def main():
    kvalue = int(sys.argv[1]) #length of k_mer
    path_to_fas = sys.argv[2]
    names = [] #sequence file names

    for name in sorted(glob.glob(path_to_fas +'/*.fa')):
        names.append(os.path.basename(name))

    countFrequencies(names,kvalue)

if __name__ == '__main__':
    main()
