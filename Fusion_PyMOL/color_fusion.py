#!/usr/bin/env python
import pymol
from pymol import cmd

# Script that colors the residues of the active site and linker in fusion
# protein system

# usage: pymol color_fusion.py -- param.txt
# param.txt - parameter file that contains values of global values

# Global variables (initialised in input file)
obj_name = 'fusion'
fusion_file = ''
first_protein = ''
first_length = ''
active_site_residues_1 = []

second_protein = ''
second_length = '' # probably unused variable
active_site_residues_2 = []

linker = ''
linker_repeats = ''
linker_length = 0

colors = []

# Do parsing of such parameters that could be passed by file
def parse_parameters(file):
    global fusion_file, first_protein, first_length, active_site_residues_1
    global second_protein, second_length, active_site_residues_2
    global linker, linker_repeats, linker_length, colors
    
    f = open(file, 'r')

    for line in f:
        line = line.replace('\n', '')
        elements = line.split(' ')
        if(elements[0] == 'fusion:'):
            fusion_file = elements[1]
            
        # Process parameters for the 1st protein
        if(elements[0] == 'protein_1:'):
            first_protein = elements[1]
        if(elements[0] == 'length_1:'):
            first_length = elements[1]
        if(elements[0] == 'active_sites_1:'):
            active_site_residues_1 = elements[1:]
            
        # Process parameters for the 2nd protein
        if(elements[0] == 'protein_2:'):
            second_protein = elements[1]
        if(elements[0] == 'length_2:'):
            second_length = elements[1]
        if(elements[0] == 'active_sites_2:'):
            active_site_residues_2 = elements[1:]
            
        # Process parameters for the linker
        if(elements[0] == 'linker:'):
            linker = elements[1]
        if(elements[0] == 'linker_repeats:'):
            linker_repeats = elements[1]
            
        # Process colors
        if(elements[0] == 'colors:'):
            colors = elements[1:]
    
    linker_length = len(linker) * int(linker_repeats)
    f.close()

def color_fusion():
    # Loading and coloring structure
    cmd.load(fusion_file, obj_name)
    cmd.color(colors[2], obj_name)

    # Selecting residues of the active site
    for i in range(len(active_site_residues_1)):
        cmd.select('resi '+active_site_residues_1[i])
        active_site_name = 'as_1_'+str(i+1)
        cmd.set_name('sele', active_site_name)
        cmd.color(colors[4], active_site_name)

    # Get length of the whole system
    # print( len( set( [(i.chain,i.resi,i.resn) for i in cmd.get_model(obj_name).atom] ) ))

    # Color the residues of the linker
    first_linker_res = int(first_length)+1
    last_linker_res = int(first_length)+linker_length
    cmd.select('resi '+str(first_linker_res)+'-'+str(last_linker_res))
    cmd.set_name('sele', 'linker')
    cmd.color(colors[5], 'linker')

    # Modifying the number of residues (accordingly to the length of first
    # protein and the linker)
    mod_active_site_residues_2 = []
    for j in range(len(active_site_residues_2)):
        sep_residues = active_site_residues_2[0].split('+')
        mod_res = ''
        for i in range(len(sep_residues)):
            sep_res_num = int(sep_residues[i])
            sep_res_num += int(first_length)
            sep_res_num += linker_length
            mod_res += str(sep_res_num)
            if(i != len(sep_residues)-1):
                mod_res += '+'
        mod_active_site_residues_2.append(mod_res)
        
    # Color the residues of the second protein active site
    for i in range(len(mod_active_site_residues_2)):
        cmd.select('resi '+mod_active_site_residues_2[i])
        active_site_name = 'as_2_'+str(i+1)
        cmd.set_name('sele', active_site_name)
        cmd.color(colors[4], active_site_name)

# Call coloring code
parse_parameters(sys.argv[1])
color_fusion()
