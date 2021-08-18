#!/usr/bin/env python
import pymol
#from pathlib import Path
from pymol import cmd
import os
import subprocess

from functions import parse_parameters, color_fusion, calculate_distance

# Script that colors the residues of the active site and linker in fusion
# protein system

# usage: pymol main.py -- param.txt
# param.txt - parameter file that contains values of global values

class Parameters():
    pass

par = Parameters()
par.obj_name = 'fusion'

# Perform coloring
parse_parameters.parse_parameters(sys.argv[1], par)

color_fusion.color_fusion(par)

# Structural alignment with homologs
# color_fusion.load_templates(par)

# Calculate distance between active sites
command = "grep 'MODEL' "+ par.fusion_file + " | wc -l"
states = int(subprocess.getstatusoutput(command)[1])
dist = [None] * states

if states > 1:
    print("Multiple states")
    calculate_distance.calculate_distance_multiple_states(par, dist)
else:
    print("One state")
    calculate_distance.calculate_distance(par, dist)

calculate_distance.write_to_file(par, dist, "./tmp/distances.txt")
