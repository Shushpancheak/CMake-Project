import sys

lines = sys.stdin.readlines().replace
index = open("index.h", "w")

for line in lines:
    line.rstrip()
    index.write("#include \"" + line + "\"")