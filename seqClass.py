#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

# Here we define arguments that we will provide in the shell
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper()                 # Note we just added this line
if re.search('^[ACGTU]+$', args.seq):
    # now we first check for sequence containning T and U before the original analysis
    if 'T' in args.seq and 'U' in args.seq:
        print('The sequence contains both T and U and should be checked')
    else:
        if re.search('T', args.seq):
            print ('The sequence is DNA')
        elif re.search('U', args.seq):
            print ('The sequence is RNA')
        else:
            print ('The sequence can be DNA or RNA')

else:
    print ('The sequence is not DNA nor RNA')

# This part look for the provided motif and tells whether or not it is in our sequence
if args.motif:
  args.motif = args.motif.upper()
  print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
  if args.motif in args.seq :
    print("trouvé")
  else:
    print("pas trouvé")
