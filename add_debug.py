#!/usr/bin/env python3

from sys import argv

with open(argv[1], 'r') as f:
  inp = f.read().splitlines()

outp = []
i = 0

for line in inp:
  if len(line) > 0:
    if line[0] == '{':
     line += 'fprintf(stderr, "{}\\n");'.format(inp[i-1].split('(')[0])
  outp.append(line)
  i += 1

with open(argv[2], "w") as f:
  print(*outp, sep="\n", file=f)
