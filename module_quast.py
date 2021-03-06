__author__ = 'mcdy143'
#!/usr/bin/env python
import os
import subprocess
import re

inputDirectory_edena = "/home/sim8/assemblyMagicResults/edena/"
inputDirectory_abyss = "/home/sim8/assemblyMagicResults/abyss/"
inputDirectory_spades = "/home/sim8/assemblyMagicResults/spades/"
inputDirectory_reference = "/home/sim8/assemblyMagicResults/reference/"
inputDirectory_cisa = "/home/sim8/assemblyMagicResults/CISA/"
folders_edena = [os.path.join(inputDirectory_edena,fn) for fn in next(os.walk(inputDirectory_edena))[1]]
folders_abyss = [os.path.join(inputDirectory_abyss,fn) for fn in next(os.walk(inputDirectory_abyss))[1]]
folders_spades = [os.path.join(inputDirectory_spades,fn) for fn in next(os.walk(inputDirectory_spades))[1]]
folders_reference = [os.path.join(inputDirectory_reference,fn) for fn in next(os.walk(inputDirectory_reference))[1]]
folders_cisa = [os.path.join(inputDirectory_cisa,fn) for fn in next(os.walk(inputDirectory_cisa))[1]]
'''
for folder in folders_edena:
    filePath = folder + "/_contigs.fasta"
    subprocess.call(["/home/agupta399/installation/quast-2.3/quast.py", "-o", folder, filePath])

for folder in folders_spades:
    filePath = folder + "/scaffolds.fasta"
    subprocess.call(["/home/agupta399/installation/quast-2.3/quast.py", "-o", folder, filePath])

for folder in folders_abyss:
    filePath = folder + "/scaffolds.fa"
    subprocess.call(["/home/agupta399/installation/quast-2.3/quast.py", "-o", folder, filePath])

for folder in folders_reference:
    filePath = folder + "/contigs.fasta"
    subprocess.call(["/home/agupta399/installation/quast-2.3/quast.py", "-o", folder, filePath])
'''
for folder in folders_cisa:
    filePath = folder + "/cisa-contig.fa"
    subprocess.call(["/home/agupta399/installation/quast-2.3/quast.py", "-o", folder, filePath])
