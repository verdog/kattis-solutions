#!/usr/bin/python2

import random

size = 1000

print(str(size) + " " + str(size))

grid = []
for i in range(0, size):
	grid.append([0] * size)

def r():
	return random.randrange(1, size)

x = 0
y = 0
grid[x][y] = 1

l = [(x, y)]

directs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def pretty_print():
	for r in range(0, size):
		line = ""
		for c in range(0, size):
			line = line + str(grid[r][c])
		print(line)

while(len(l)):
	e = l.pop(random.randrange(0, len(l)))
	for direct in directs:
		X = e[0] + direct[0] * 2
		Y = e[1] + direct[1] * 2
		if(0 <= X and X < size and 0 <= Y and Y < size):
			if(grid[X][Y] == 0):
				grid[X - direct[0]][Y - direct[1]] = 1
				grid[X][Y] = 1
				l.append((X, Y))
pretty_print()

print("1000")
for i in range(0, 1000):
	c = []
	for f in range(0, 4):
		c.append(r())
	print(str(c[0]) + " " + str(c[1]) + " " + str(c[2]) + " " + str(c[3]))
