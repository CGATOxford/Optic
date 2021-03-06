##########################################################################
#
#   MRC FGU Computational Genomics Group
#
#   $Id: cgat_script_template.py 2871 2010-03-03 10:20:44Z andreas $
#
#   Copyright (C) 2009 Andreas Heger
#
#   This program is free software; you can redistribute it and/or
#   modify it under the terms of the GNU General Public License
#   as published by the Free Software Foundation; either version 2
#   of the License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
##########################################################################
'''
cgat_script_template.py
=============================================

:Author: 
:Release: $Id$
:Date: |today|
:Tags: Python

Purpose
-------

convert cd-hit clusters file to tab separated file.

Usage
-----

Example::

   python cgat_script_template.py --help

Type::

   python cgat_script_template.py --help

for command line help.

Documentation
-------------

Code
----

'''

import sys
import os
import re
import optparse

import CGAT.Experiment as E
import CGAT.Genomics as Genomics


def main(argv=None):
    """script main.

    parses command line options in sys.argv, unless *argv* is given.
    """

    if not argv:
        argv = sys.argv

    # setup command line parser
    parser = E.OptionParser(version="%prog version: $Id: cgat_script_template.py 2871 2010-03-03 10:20:44Z andreas $",
                            usage=globals()["__doc__"])

    # add common options (-h/--help, ...) and parse command line
    (options, args) = E.Start(parser, argv=argv)

    map_rep2mem, map_mem2rep = Genomics.ReadClusters(sys.stdin)

    #  print all members
    for k in map_mem2rep.keys():
        print "%s\t%s" % (k, map_mem2rep[k])

    # print all representatives
    for k in map_rep2mem.keys():
        print "%s\t%s" % (k, k)

    # write footer and output benchmark information.
    E.Stop()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
