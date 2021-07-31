# GenFusMSA

GenFusMSA is a script that generates multiple sequence alignment (MSA) file that can be used 
for fusion protein joined via linkers of choice modelling. This program supports [small tool for 
bioinformatics manifesto](https://github.com/pjotrp/bioinformatics).

## Requirements

Download and install [Perl](https://www.perl.org/get.html).

## Usage

Inputs for this program are:  
1. Full query-template .a3m file of the first protein  
2. Full query-template .a3m file of the second protein  
3. Peptide linker sequence
4. Repeats of the linker
5. Option to extend the linker with 

These .a3m files can be generated using external software. The program was tested with MSA
files that were generated using [HHblits](https://toolkit.tuebingen.mpg.de/tools/hhblits) program. 

`perl GenFusMSA.pl 4CL_fullQT.a3m CHS_fullQT.a3m EAAAK 1`  

This command generates MSA file for 4CL and CHS linked via prolonged EAAAK linker. The 
option to choose prolonged linker by glycines (by 10 on both sides of the linker) is set by the 
last option (0 or 1).


