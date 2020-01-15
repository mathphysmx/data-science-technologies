#!C:/Users/panch/Miniconda3/envs/intelgraph/python.exe

# This file shows how to execute a script from command line (terminal)

## usage:
# # Windows 10
#     py .\code\argparseexample.py --filepath "./data/source/Mascara archivo plano Sep-2019.xlsx"
# # Linux
#        ./code/argparseexample.py --filepath "./data/source/Mascara archivo plano Sep-2019.xlsx"

## Tutorials
# http://zetcode.com/python/argparse/
    # WINDOWS 10:
        # https://www.ryansmccoy.com/2016/07/16/python-setting-up-windows-shebang-using-anaconda/
        # https://stackoverflow.com/questions/51861943/how-to-install-python-launcher

## For debugging:
# import sys
# version = sys.version.split()[0]
# print(version)

import argparse, os
import pandas as pd

# help flag provides flag help
# store_true actions stores argument as True

# os.path.isdir("./data/source")
# os.getcwd()
# os.path.isfile("./data/source/Mascara archivo plano Sep-2019.xlsx")
parser = argparse.ArgumentParser()
   
parser.add_argument('-o', '--output', action='store_true', 
    help="shows output")
parser.add_argument('--filepath', required=True)
args = parser.parse_args()

if os.path.isfile(args.filepath):
    print(f'Hello {args.filepath}')

if args.output:
    print("This is some output")