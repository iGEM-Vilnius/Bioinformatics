#!/usr/bin/env python
import pymol
from pathlib import Path
from pymol import cmd

import parse_parameters
import color_fusion
import center_of_mass

# Script that colors the residues of the active site and linker in fusion
# protein system

# usage: pymol color_fusion.py -- param.txt
# param.txt - parameter file that contains values of global values

class Parameters():
    pass

par = Parameters()
par.obj_name = 'fusion'

# Subroutine that calculates distance between active sites
def calculate_distance():
    center_of_mass.com('as_1_1', 1, 'COM_1')
    center_of_mass.com('as_2_1', 1, 'COM_2')
    cmd.distance('distance_COM', 'as_1_1_COM', 'as_2_1_COM')
    
    cmd.set('label_color', colors[0], 'distance_COM')
    cmd.color(colors[4], 'distance_COM')
    
# Subroutine that loads template files
def load_templates():
    cmd.load(first_protein)
#    print(os.path.splitext(first_protein)[0])
    first_prot_name = Path(first_protein).stem
    cmd.color(colors[3], first_prot_name)
    cmd.load(second_protein)
    second_prot_name = Path(second_protein).stem
    cmd.color(colors[0], second_prot_name)
    
    cmd.cealign(obj_name, first_prot_name)
    cmd.cealign(obj_name, second_prot_name)
    cmd.center(obj_name)

# Call coloring code
parse_parameters.parse_parameters(sys.argv[1], par)
color_fusion.color_fusion(par)
#calculate_distance()
#load_templates()
