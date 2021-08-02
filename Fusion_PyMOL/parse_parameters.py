#!/usr/bin/env python

# Do parsing of such parameters that could be passed by file
def parse_parameters(file, par):
#    global fusion_file, first_protein, first_length, active_site_residues_1
#    global second_protein, second_length, active_site_residues_2
#    global linker, linker_repeats, linker_length, colors
    
    f = open(file, 'r')

    for line in f:
        line = line.replace('\n', '')
        elements = line.split(' ')
        if(elements[0] == 'fusion:'):
            par.fusion_file = elements[1]

        # Process parameters for the 1st protein
        if(elements[0] == 'protein_1:'):
            par.first_protein = elements[1]
        if(elements[0] == 'length_1:'):
            par.first_length = elements[1]
        if(elements[0] == 'active_sites_1:'):
            par.active_site_residues_1 = elements[1:]

        # Process parameters for the 2nd protein
        if(elements[0] == 'protein_2:'):
            par.second_protein = elements[1]
        if(elements[0] == 'length_2:'):
            par.second_length = elements[1]
        if(elements[0] == 'active_sites_2:'):
            par.active_site_residues_2 = elements[1:]

        # Process parameters for the linker
        if(elements[0] == 'linker:'):
            par.linker = elements[1]
        if(elements[0] == 'linker_repeats:'):
            par.linker_repeats = elements[1]

        # Process colors
        if(elements[0] == 'colors:'):
            par.colors = elements[1:]

    par.linker_length = len(par.linker) * int(par.linker_repeats)
    f.close()

