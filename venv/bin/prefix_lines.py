#!/home/hope/New_Galaxy/galaxy_app_test/venv/bin/python3

"""
Simple script to add a prefix to every line in a file.
"""

import sys

for line in sys.stdin:
    print(sys.argv[1] + line, end=" ")
