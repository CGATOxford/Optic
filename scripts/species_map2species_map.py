'''
species_map2species_map.py
=============================================

:Author: Nick Ilott
:Release: $Id$
:Date: |today|
:Tags: Python

Purpose
-------

Convert species ids from a species_map file to names provided from 
genome files.

Usage
-----

Example::

   python species_map2species_map.py --help

Type::

   python species_map2species_map.py --help

for command line help.

Documentation
-------------

This is a script with a very specific purpose. Read names that are sampled from
many genomes using GemReads.py are by default converted into substrings of the 
original strings. For sampling contigs using contigs2random_sample.py we require
a species map file with names that correspond to the genomes being simulated.
Therefore this script converts names back to original genome style names using
gi number as the common identifier.

Reads from stdin and outputs to stdout.

Command line options
--------------------

'''

import os
import sys
import re
import optparse
import CGAT.FastaIterator as FastaIterator
import glob
import CGAT.Experiment as E
import CGAT.IOTools as IOTools


def main(argv=None):
    """script main.

    parses command line options in sys.argv, unless *argv* is given.
    """

    if not argv:
        argv = sys.argv

    # setup command line parser
    parser = optparse.OptionParser(version="%prog version: $Id: script_template.py 2871 2010-03-03 10:20:44Z andreas $",
                                   usage=globals()["__doc__"])

    parser.add_option("-g", "--genome-dir", dest="genome_dir", type="string",
                      help="supply help")

    # add common options (-h/--help, ...) and parse command line
    (options, args) = E.Start(parser, argv=argv)

    contigs_map = {}
    for genome in glob.glob(os.path.join(options.genome_dir, "*")):
        for fasta in FastaIterator.iterate(IOTools.openFile(genome)):
            identifier = fasta.title.split("|")
            gi = identifier[1]
            contigs_map[gi] = fasta.title

    for line in options.stdin.readlines():
        data = line[:-1].split("\t")
        gi = data[1]
        assert gi in contigs_map, "cannot find genome with id gi|%s in genomes directory" % gi

        options.stdout.write("%s\t%s\n" % (data[0], contigs_map[gi]))

    # write footer and output benchmark information.
    E.Stop()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
