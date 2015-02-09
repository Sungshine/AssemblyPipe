__author__ = 'sungshine'
#!/usr/bin/python3
#Invokes prinseq-lite on raw read files using default settings passing files in as argument

import os
import sys
import subprocess

inputDirectory = sys.argv[1]    #/home/biol8803b/data
outputDirectory = sys.argv[2]   #/home/biol8803b/preProcessed
paths = [os.path.join(inputDirectory,fn) for fn in next(os.walk(inputDirectory))[2]]

def modulePrinseq(file, outputDirectory):
    subprocess.call(['prinseq-lite', '-verbose', '-fastq', file, '-out_format','3', '-out_good', outputDirectory,])

# modulePrinseq(file, outputDirectory)