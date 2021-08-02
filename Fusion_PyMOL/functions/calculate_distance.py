#!/usr/bin/env python
import pymol
from pymol import cmd
from functions import center_of_mass

# Subroutine that calculates distance between active sites when rigid linker
# is used in the fusion protein system
def calculate_distance(par):
    center_of_mass.com('as_1_1', 1, 'COM_1')
    center_of_mass.com('as_2_1', 1, 'COM_2')
    cmd.distance('distance_COM', 'as_1_1_COM', 'as_2_1_COM')
    
    cmd.set('label_color', par.colors[0], 'distance_COM')
    cmd.color(par.colors[4], 'distance_COM')
