import sys
import argparse
import os

parser = argparse.ArgumentParser('Generate index.h')
parser.add_argument('--dir', help='Output directory', required=True)

args = parser.parse_args()

os.makedirs(args.dir, exist_ok=True)

index = open(os.path.join(args.dir, "index.h"), "w")

index.write("#pragma once\n")
index.write("namespace index {\n")
index.write("void CheckThatIndexIsWorking();\n")
index.write("}\n")

print("preparing.py :: Created index.h")

index.close()