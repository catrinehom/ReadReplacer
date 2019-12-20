#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 10:36:28 2019

@author: catrinehom
"""


# Import libraries 
import sys
from argparse import ArgumentParser

###########################################################################
# FUNCTIONS
###########################################################################

def OpenFile(filename,mode):
    '''
    This function opens the input file in chosen mode.
    '''
    try:
        infile = open(filename,mode)   
    except IOError as error:
        print('Could not open '+filename+' due to: '+str(error))
        sys.exit(1)
    return infile

###########################################################################
# GET INPUT
###########################################################################

# Input from command line
parser = ArgumentParser()
parser.add_argument('-a', dest='all_fastq',help='Input file to find IDs from')
parser.add_argument('-b', dest='high_quality_fastq', help='Output filename')
args = parser.parse_args()

# Define input as variables
all_fastq_filename = args.all_fastq
high_quality_fastq_filename = args.high_quality_fastq

all_fastq_filename = './test.fastq'
high_quality_fastq_filename = './test_HAC.fastq'

# Open files
all_fastq_filename = OpenFile(all_fastq_filename,'r')
high_quality_fastq = OpenFile(high_quality_fastq_filename,'r')

high_quality_fastq_set = set()

for line in high_quality_fastq:
    if line.startswith('@'):
        high_quality_fastq_set.add(line.split()[0])
        
        
high_quality_fastq.close()   

# Open output file for mot matching reads:    
outfilename = 'final.fastq'
flag = False

try:
    outfile = open(outfilename,'w')
except IOError as error:
    sys.stdout.write('Could not write file due to: '+str(error))
    sys.exit(1)

for line in all_fastq_filename:
    if line.startswith('@'):
        if line.split()[0] in high_quality_fastq_set:
            flag = False
        else:
            flag = True
    if flag == True:
        print(line,file=outfile, end = '')
        
#.decode('ascii')

high_quality_fastq = OpenFile(high_quality_fastq_filename,'r')
        
for line in high_quality_fastq:
    print(line,file=outfile, end = '')

outfile.close()
