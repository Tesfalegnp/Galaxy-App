#!/home/hope/New_Galaxy/galaxy_app_test/venv/bin/python3

"""
Read a wiggle track and print out a series of lines containing
"chrom position score". Ignores track lines, handles bed, variableStep
and fixedStep wiggle lines.
"""

import sys

import bx.wiggle

if len(sys.argv) > 1:
    in_file = open(sys.argv[1])
else:
    in_file = sys.stdin

if len(sys.argv) > 2:
    out_file = open(sys.argv[2], "w")
else:
    out_file = sys.stdout

for fields in bx.wiggle.Reader(in_file):
    print(" ".join(map(str, fields)))

in_file.close()
out_file.close()
