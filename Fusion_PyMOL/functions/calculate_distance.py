#!/usr/bin/env python
import pymol
from pymol import cmd
from functions import center_of_mass

# Subroutine that calculates distance between active sites when rigid linker
# is used in the fusion protein system
def calculate_distance(par, state=1):
    COM_1 = 'COM_1_'+str(state)
    COM_2 = 'COM_2_'+str(state)
    center_of_mass.com('as_1_1', None, None, COM_1, 0)
    center_of_mass.com('as_2_1', None, None, COM_2, 0)
    cmd.distance('distance_COM', COM_1, COM_2)
    cmd.create('ov_COM_1', COM_1, 0, state)
    cmd.create('ov_COM_2', COM_2, 0, state)
    cmd.delete(COM_1)
    cmd.delete(COM_2)
    
    cmd.set('label_color', par.colors[0], 'distance_COM')
    cmd.color(par.colors[4], 'distance_COM')
