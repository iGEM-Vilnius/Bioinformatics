#!/usr/bin/perl

use strict;
use warnings;

# Script that extracts from two MSA files sequences that share the same TaxID.

# Input: two MSA (.a3m) files, linker, boolean option to enlong linker

# Prolonged linker has 10 glycine residues on both sides.

# Output: one MSA file (.a3m) for fusion protein modelling

# Example run: ./generate_msa.pl 4CL_fullQT.a3m CHS_fullQT.a3m EAAAK 1
# After running this command the prolonged MSA when linker is EAAAK is printed
# to the terminal window.

my $in1 = shift @ARGV;
my $in2 = shift @ARGV;
my $linker = shift @ARGV;
my $prolonged = shift @ARGV;

my %taxid_1 = ();
my %matched = ();

my $num1 = 0;
my $num2 = 0;

# Reading the first input .a3m file
open(my $inp, '<', $in1);
$/ = "\n>";
while( <$inp> ) {
    /^>?([^\n]*)\n([^>]*)/;
    my( $header, $sequence ) = ( $1, $2 );
    $sequence =~ s/\s//g;
    if($sequence){
        $num1 += 1;
        if($num1 == 1){
            my $taxid = 'query';
            $taxid_1{$taxid} = $sequence;
        }else{
            my @split_header = split(' ', $header);
            $header =~ /TaxID=([[:digit:]]+)/;
            my $taxid = $1;
            $taxid_1{$taxid} = $sequence if($taxid);
        }
    }
}
close($inp);

# Reading the second input .a3m file
open($inp, '<', $in2);
while( <$inp> ) {
    /^>?([^\n]*)\n([^>]*)/;
    my( $header, $sequence ) = ( $1, $2 );
    $sequence =~ s/\s//g;
    if($sequence){
        $num2 += 1;
        if($num2 == 1){
            my $taxid = 'query';
            $matched{$taxid} = $taxid_1{$taxid} . $sequence;
        }else{
            my @split_header = split(' ', $header);
            $header =~ /TaxID=([[:digit:]]+)/;
            my $taxid = $1;
            if($taxid && exists($taxid_1{$taxid})){
                # Merging sequences that have got matching TaxIDs
                # in both input MSA
                my $merged_seq = $taxid_1{$taxid};
                $merged_seq .= $sequence;
                # Adding merged sequence to the array for the result
                $matched{$taxid} = $merged_seq;
            }
        }
    }
}
close($inp);

# Determining the length of the longest construct
my $max_length = 0;
for my $id (keys(%matched)){
    $max_length = length($matched{$id}) if(length($matched{$id}) > $max_length);
}

# Adding the linker to the output MSA
for my $id (reverse sort keys(%matched)){
    my $fusion = substr($matched{$id}, 0, length($taxid_1{$id}));
    if($prolonged){
        $fusion .= 'G' x 10;
        $fusion .= $linker;
        $fusion .= 'G' x 10;
    }else{
        $fusion .= $linker;
    }
    
    $fusion .= substr($matched{$id}, length($taxid_1{$id}), length($matched{$id}));
    
    $matched{$id} = $fusion;
    
    # Printing output MSA
    print '>', $id, "\n", $matched{$id}, "\n";
}
