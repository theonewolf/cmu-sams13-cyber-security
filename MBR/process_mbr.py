#!/usr/bin/env python
###############################################################################
#                                                                             #
#   This file crawls the MBR of a raw disk image.                             #
#                                                                             #
#   Author: Wolfgang Richter <wolf@cs.cmu.edu>                                #
#   License: MIT                                                              #
#                                                                             #
###############################################################################


from collections    import namedtuple
from struct         import calcsize, unpack_from
from sys            import stderr,argv
from termcolor      import colored



# global definitions
MBR         =   namedtuple('MBR', 'bootcode pt signature') 
PTE         =   namedtuple('PTE', 'status CHS type CHSaddress start length')

MBR_FMT     =   '''<446s64sH'''
PTE_FMT     =   '''<B3sB3sII'''

MBR_SIZE    =   calcsize(MBR_FMT)
PTE_SIZE    =   calcsize(PTE_FMT)

PTE_TYPES   =   {0x83 : 'Linux'}



# utility printing helpers
def print_field_name(field):
    print colored('\t%s' % field, 'blue')

def print_field(field):
    print colored('\t|', 'blue'),
    print colored(field, 'yellow')

def bytes_to_int(s):
    return int(s.encode('hex'), 16)



# struct printers
def print_mbr(mbr):
    print_field_name('MBR')
    print_field('MBR.signature : 0x%0.4x' % (mbr.signature))

def print_pte(pte, i):
    if (pte.type | pte.status):
        print_field_name('PTE[%d]' % i)
        print_field('Status : 0x%0.2x' % pte.status)
        print_field('CHS : 0x%0.6x' % bytes_to_int(pte.CHS))
        print_field('Type : 0x%0.2x' % pte.type)
        print_field('CHS Start : 0x%0.6x' % bytes_to_int(pte.CHSaddress)) 
        print_field('LBA Start : 0x%0.8x' % pte.start)
        print_field('Length : 0x%0.8x' % pte.length)



# utility functions 
def check_mbr(mbr):
    return mbr.signature == 0xaa55



# main thread of execution logic
if __name__ == '__main__':
    if len(argv) < 2:
        stderr.write('Not enough arguments.  Please provide a file name.\n')
        exit(1)

    print colored('Processing: %s' % argv[1], 'red')

    with open(argv[1], 'r') as f:
        data = f.read(MBR_SIZE)
        mbr = MBR._make(unpack_from(MBR_FMT, data))
        
        print_mbr(mbr)

        if (check_mbr(mbr)):
            print colored('--> MBR Check passed', 'green')
            for i in xrange(4):
                pte = PTE._make(unpack_from(PTE_FMT, mbr.pt, i*PTE_SIZE))
                print_pte(pte, i)
