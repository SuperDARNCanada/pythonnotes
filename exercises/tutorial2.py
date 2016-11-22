"Tutorial 2 file IO example"

import sys

file_name = sys.argv[1]

data = []
with open(file_name,'r') as f:
    data = f.readlines()


numeric_data = []
for line in data:
    print(line.split())

    for n in line.split():
        numeric_data.append(int(n))

print(numeric_data)