#! /usr/bin/env python
import sys

infile, outfile = sys.argv[1], sys.argv[2]
inf,outf = open(infile), open(outfile,"w")

outf.write("digraph \"" + infile + "\" {\n")

for line in inf.readlines():
    if "#" not in line:
        if ".connect_to" in line:
            splitted = line.lstrip().split(".connect_to ")
            sourceSplit = splitted[0].split(".")
            targetSplit = splitted[1].split(".")
            sourceNode,sourcePort = sourceSplit[0],sourceSplit[1]
            targetNode,targetPort = targetSplit[0],targetSplit[1]
            outf.write(sourceNode + " -> " + targetNode + "[ taillabel=\"" + sourcePort + "\"" + " headlabel=\"" + targetPort + "\""+ "];\n")

outf.write("}\n")

inf.close()
outf.close()
