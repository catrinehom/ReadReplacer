#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 10:36:28 2019

@author: catrinehom
"""


# Import libraries 
import sys
import time
from argparse import ArgumentParser

###########################################################################
# FUNCTIONS
###########################################################################

def CheckGZip(filename):
    '''
    This function checks if the input file is gzipped.
    '''
    gzipped_type = b'\x1f\x8b'
    
    infile = open(filename,'rb')
    filetype = infile.read(2)
    infile.close()
    if filetype == gzipped_type:
        return True
    else:
        return False
    
def CheckFastq(filenames):
    """
    This function checks if a input file is in fastq format.
    Outputs True/False for the file.
    """
    fastq_type = "@"

    # Open all files and get the first character
    for infile in filenames:
        f = OpenFile(infile, "r")
        first_char = f.read(1);
        f.close()
        # Check if fastq
        if first_char == fastq_type:
            fastq = True
        else:
            fastq = False
    return fastq


def OpenFile(filename,mode):
    '''
    This function opens the input file in chosen mode.
    '''
    try:
        infile = open(filename,mode)   
    except IOError as error:
        message = 'Could not open '+filename+' due to: '+str(error)
        sys.exit(message)
    return infile

###########################################################################
# GET INPUT
###########################################################################

# Input from command line
parser = ArgumentParser()
parser.add_argument('-a', dest='all_fastq',help='File with all fastq reads.')
parser.add_argument('-q', dest='high_quality_fastq', help='File with fastq reads to replace in all fastq file.')
parser.add_argument('-o', dest='outfilename', help='Output filename.')
args = parser.parse_args()

###########################################################################
# ERROR HANDLING
###########################################################################

# Define input as variables
if args.all_fastq is None:
    all_fastq_filename = args.all_fastq
else:
    message = '-a option is missing. Please input a file with all fastq reads.'
    sys.exit(message)
    
if args.high_quality_fastq is None:
    high_quality_fastq_filename = args.high_quality_fastq
else:
    message = '-q option is missing. Please input a file with fastq reads to replace in all fastq file.'
    sys.exit(message)
    
if args.outfilename is None:
    outfilename = args.outfilename
else:
    message = '-o option is missing. Please input a output filename.'
    sys.exit(message)
    

# Check if input files are in zipped
a_check_zipped = CheckGZip(all_fastq_filename)
h_check_zipped = CheckGZip(high_quality_fastq_filename)

# Exit if the input files are not in fastq format
if a_check_zipped is True:
    message = "Input Error: {} is zipped. Unzip file to run pipeline.".format(all_fastq_filename)
    sys.exit(message)

if h_check_zipped is True:
    message = "Input Error: {} is zipped. Unzip file to run pipeline.".format(high_quality_fastq_filename)
    sys.exit(message)

# Check if input files are in fastq format
a_check_fastq = CheckFastq(all_fastq_filename)
h_check_fastq = CheckFastq(high_quality_fastq_filename)


# Exit if the input files are not in fastq format
if a_check_fastq is False:
    message = "Input Error: {} is a wrong format. Should be fasta format.".format(all_fastq_filename)
    sys.exit(message)

if h_check_fastq is False:
    message = "Input Error: {} is a wrong format. Should be fasta format.".format(high_quality_fastq_filename)
    sys.exit(message)

# Start runtimer for program
runtime_start = time.time()

###########################################################################
# FIND REPLACEMENT NAMES
###########################################################################

# Open files
all_fastq_filename = OpenFile(all_fastq_filename,'r')
high_quality_fastq = OpenFile(high_quality_fastq_filename,'r')

high_quality_fastq_set = set()

for line in high_quality_fastq:
    if line.startswith('@'):
        high_quality_fastq_set.add(line.split()[0])
        
        
high_quality_fastq.close()   


###########################################################################
# SAVE TO NEW FILE
###########################################################################

# Open output file for mot matching reads:    
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


high_quality_fastq = OpenFile(high_quality_fastq_filename,'r')
        
for line in high_quality_fastq:
    print(line,file=outfile, end = '')

outfile.close()


print(outfilename+' is saved with replaced reads.')

# End runtimer for program and print
runtime_end = time.time()
print('Runtime: {0:.0f} seconds.'.format(runtime_end-runtime_start))
