#!/home/hope/New_Galaxy/galaxy_app_test/venv/bin/python3

"""
Script to select random lines from a file. Reads entire file into
memory!

TODO: Replace this with a more elegant implementation.
"""

import random
import sys

ndesired = int(sys.argv[1])

for line in random.sample(sys.stdin.readlines(), ndesired):
    print(line, end=" ")
