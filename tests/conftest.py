import os
import sys

#Add repo folder to the python path so we can look for modules there
root = os.path.dirname(os.path.realpath('__file__'))
sys.path.insert(0, root)