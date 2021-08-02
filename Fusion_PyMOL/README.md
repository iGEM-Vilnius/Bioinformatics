# Fusion PyMOL
This directory contains several tools to use for fusion protein processing. 

## color_fusion.py
A script that colors fusion protein system: the whole construct, the linker, and the active sites 
of each of the fused proteins.  

### Usage

The coloring is done using:  
`pymol color_fusion.py -- param.txt`  

### Customization

All configurations about the coloring are written in `param.txt` file. This file contains attributes 
that are labelled as:  
* `fusion:` path to the PDB file of the fusion construct  
* `protein_1:` path to the PDB file of the first protein in the fusion  
* `length_1:` length of the first protein (residues)  
* `active_sites_1:` residues that form active sites of the first protein (residues in the same 
active site are separated with `+`, different active sites are separated with whitespace)  
* `protein_2:` path to the PDB file of the second protein in the fusion
* `length_2:`  length of the second protein (residues)  
* `active_sites_2:` residues that form active sites of the second protein (residues in the same 
active site are separated with `+`, different active sites are separated with whitespace)  
* `linker:` residues that compose the linker  
* `linker_repeats:` how many times the `linker` residues are used  
* `colors:`  colors given in hex code that are used to color the system (more information below)

It should be noted that after each attribute a colon `:` symbol should be added.  
Additionally there is an example of such file deposited in this repository:  

```
fusion: PDB/GSG_after_md.pdb

protein_1: PDB/templates/N_term.pdb
length_1: 562
active_sites_1: 251+278+279 163+461

protein_2: PDB/templates/C_term.pdb
length_2: 395
active_sites_2: 309+342+347

linker: GSG
linker_repeats: 1

colors: 0x002733 0x054d54 0x1b8489 0xef9f8d 0xfccec0 0x00fbff
```

