__author__ = 'sungshine'
#!/usr/bin/env python
#assemblyMagic beta version

import getopt, sys
import os
import subprocess

#list of modules

def wranglePairedEnds(prinseqPaths):
    for file in prinseqPaths:
        newfile = ""
        if "R1" in file:
            newfile = file.replace("R1", "R*")
        elif "R2" in file:
            newfile = file.replace("R2", "R*")
        if not newfile in fileHash:
            fileHash[newfile] = [file]
        else:
            fileHash[newfile].append(file)
    return

def moduleFastQC(file):
    subprocess.call(['fastqc', "-o", ODfastqc, file,])

def modulePrinseq(file):
    base = os.path.basename(file)
    filename = os.path.splitext(base)[0]
    subprocess.call(['prinseq-lite', '-verbose', '-fastq', file, '-out_format','3', '-out_good', ODprinseq+filename+".prinseq", "-out_bad", ODerrors+filename+".bad.prinseq",])

def preProcess(paths):
    for file in paths:
        moduleFastQC(file)
        modulePrinseq(file)

def moduleSpadesSE(inputfileOne):
    base = os.path.basename(inputfileOne)
    filename = os.path.splitext(base)[0]
    subprocess.call(["spades.py", "--careful", "-s", inputfileOne, "-o", ODspades+filename+".spades",])

def moduleSpadesPE(inputfileOne, inputfileTwo):
    base = os.path.basename(inputfileOne)
    filename = os.path.splitext(base)[0]
    subprocess.call(["spades.py", "--careful", "-1", inputfileOne, "-2", inputfileTwo, "-o", ODspades+filename+".spades",])

########################################################################################################################
###                                                   MAIN PROGRAM                                                   ###
########################################################################################################################

inputDirectory = "/home/sim8/test.data/"
outputDirectory = "/home/sim8/assemblyMagicResults/"

ODerrors = "/home/sim8/assemblyMagicResults/errors/"
ODprinseq = "/home/sim8/assemblyMagicResults/prinseq/"
ODfastqc = "/home/sim8/assemblyMagicResults/fastQCresults/"
ODspades = "/home/sim8/assemblyMagicResults/spades/"

prinseqHash = "/home/sim8/assemblyMagicResults/prinseq/"
fileHash = {}

paths = [os.path.join(inputDirectory,fn) for fn in next(os.walk(inputDirectory))[2]]

preProcess(paths)

prinseqPaths = [os.path.join(prinseqHash,fn) for fn in next(os.walk(prinseqHash))[2]]

wranglePairedEnds(prinseqPaths)

inputfileOne = ""
inputfileTwo = ""

for key in fileHash:

    hashValues = fileHash.get(key)
    sortedValues = sorted(hashValues)

    if len(sortedValues) == 1:
        inputfileOne = sortedValues[0]
        moduleSpadesSE(inputfileOne)

    if len(sortedValues) == 2:
        inputfileOne = sortedValues[0]
        inputfileTwo = sortedValues[1]
        moduleSpadesPE(inputfileOne, inputfileTwo)

#Do not edit this file