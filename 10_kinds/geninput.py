#!/usr/bin/python3

import random

rows = random.randint(1000, 1000)
columns = random.randint(1000, 1000)

print(rows, columns)

for r in range(rows):
    for c in range(columns):
        print(random.randint(0, 1), end='')
    print()

queries = random.randint(1000, 1000)

print(queries)

for i in range(queries):
    r1 = random.randint(1, rows)
    c1 = random.randint(1, columns)
    r2 = random.randint(1, rows)
    c2 = random.randint(1, columns)
    print(r1, c1, r2, c2)