#!/usr/bin/env python
import pymol
from pathlib import Path
from pymol import cmd

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
for i in range(1, 100):
    calculate_distance.calculate_distance(par, i)
