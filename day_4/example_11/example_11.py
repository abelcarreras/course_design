#!/usr/bin/env python
import argparse
from main import CoreProgram
from fileio import read_xyz_file


parser = argparse.ArgumentParser(description='MyProgram')
# Positional arguments
parser.add_argument(type=str,
                    dest='input_file',
                    default=None,
                    help='xyz file containing a molecule')

# Main options
parser.add_argument('-p',
                    default=None,
                    metavar='title',
                    type=str,
                    help='print molecular info')

parser.add_argument('--spaces',
                    type=int,
                    default=3,
                    help='spaces between title and coordinates')
parser.add_argument('-v', '--version',
                    dest='version',
                    action='store_true',
                    default=False,
                    help='print version number')

args = parser.parse_args()

symbols, coordinates = read_xyz_file(args.input_file)
core = CoreProgram(symbols, coordinates)

if args.p is not None:
    result = core.print_molecule_info(args.p, spaces=args.spaces)

if args.version is True:
    from main import __version__
    print(__version__)
