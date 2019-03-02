import sys

index = open("index.h", "w")

index.write("#pragma once")
index.write("namespace index {")
index.write("void CheckThatIndexIsWorking();")
index.write("}")

print("created index.h")