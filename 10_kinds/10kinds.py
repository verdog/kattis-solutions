#!/usr/bin/python3

from sys import setrecursionlimit
from collections import deque

class GridUnit():
    def __init__(self, kind):
        self.kind = kind
        self.row = -1
        self.column = -1
        self.string = kind

        # zone:
        # 0 = binary
        # 1 = decimal
        # -1 = undefined
        self.zone = -1

    def __str__(self):
        return self.string

class Map():
    def __init__(self):
        self.rows = 0
        self.columns = 0
        self.map = {} # map[(row, column)] = GridUnit
        self.next_new_zone = 0 # identifier for a zone
        self.proccess_list = deque()

    def build(self):
        # rows and columns
        input_row = input()
        self.rows = int(input_row.split()[0])
        self.columns = int(input_row.split()[1])
        self.remaining = self.rows * self.columns
        # print(self.rows, self.columns)

        # build map
        for r in range(self.rows):
            input_row = input()
            for c in range(self.columns):
                self.map[(r, c)] = GridUnit(int(input_row[c]))
                if input_row[c] == '0':
                    self.map[(r, c)].string = '#'
                else:
                    self.map[(r, c)].string = '.'
                    
                self.map[(r, c)].row = r
                self.map[(r, c)].column = c

        # self.print_map()
        # print()

        # process map
        self.proccess_map()

        # self.print_map()

    def print_map(self):
        for r in range(self.rows):
            for c in range(self.columns):
                print(self.map[(r, c)], end='')
            print() # newline

    def proccess_map(self):
        self.proccess_list.append(self.map[(0, 0)])

        self.map[(0, 0)].string = '@'

        # self.print_map()
        # print()

        while not len(self.proccess_list) == 0:
            gridunit = self.proccess_list.popleft()
            if gridunit.zone == -1:
                self.fill_zone(gridunit)
                self.next_new_zone += 1
                # self.print_map()
                # print()
        
        # while len(self.proccess_map) != 0:
        
        # for r in range(self.rows):
        #     if self.remaining <= 0:
        #         break
        #     for c in range(self.columns):
        #         if self.remaining <= 0:
        #             break
        #         gridunit = self.map[(r, c)]
        #         if gridunit.zone == -1:
        #             # undefined zone. process.
        #             self.fill_zone(gridunit)

        #             # update next new zone
        #             self.next_new_zone += 1
        #         else:
        #             # definied zone. skip!
        #             continue
    
    def fill_zone(self, start_point: GridUnit):
        if start_point.zone == -1:
            start_point.zone = self.next_new_zone
            self.remaining -= 1
            start_point.string = chr(0x41 + self.next_new_zone) # start labeling at A
        else:
            return

        if self.remaining <= 0:
            return

        # try north
        if self.valid_location(start_point.row - 1, start_point.column):
            target_gridunit = self.map[(start_point.row - 1, start_point.column)]
            if target_gridunit.zone == -1 and target_gridunit.kind == start_point.kind:
                self.fill_zone(target_gridunit)
            elif target_gridunit.zone == -1 and target_gridunit.kind != start_point.kind:
                target_gridunit.string = '@'
                self.proccess_list.append(target_gridunit)

        # try south
        if self.valid_location(start_point.row + 1, start_point.column):
            target_gridunit = self.map[(start_point.row + 1, start_point.column)]
            if target_gridunit.zone == -1 and target_gridunit.kind == start_point.kind:
                self.fill_zone(target_gridunit)
            elif target_gridunit.zone == -1 and target_gridunit.kind != start_point.kind:
                target_gridunit.string = '@'
                self.proccess_list.append(target_gridunit)

        # try east
        if self.valid_location(start_point.row, start_point.column + 1):
            target_gridunit = self.map[(start_point.row, start_point.column + 1)]
            if target_gridunit.zone == -1 and target_gridunit.kind == start_point.kind:
                self.fill_zone(target_gridunit)
            elif target_gridunit.zone == -1 and target_gridunit.kind != start_point.kind:
                target_gridunit.string = '@'
                self.proccess_list.append(target_gridunit)

        # try west
        if self.valid_location(start_point.row, start_point.column - 1):
            target_gridunit = self.map[(start_point.row, start_point.column - 1)]
            if target_gridunit.zone == -1 and target_gridunit.kind == start_point.kind:
                self.fill_zone(target_gridunit)
            elif target_gridunit.zone == -1 and target_gridunit.kind != start_point.kind:
                target_gridunit.string = '@'
                self.proccess_list.append(target_gridunit)
        
    def valid_location(self, row, column):
        if row < 0:
            return False
        if row >= self.rows:
            return False
        if column < 0:
            return False
        if column >= self.columns: 
            return False
        return True
    
    def query(self, r1, c1, r2, c2):
        if self.map[(r1, c1)].zone == self.map[(r2, c2)].zone:
            print("decimal") if self.map[(r1, c1)].kind == 1 else print("binary")
        else:
            print("neither")

setrecursionlimit(10000)

gridmap = Map()
gridmap.build()

number_of_queries = int(input())

for i in range(number_of_queries):
    query_string = input().split()
    query_string = list(map(lambda q: int(q) - 1, query_string))
    gridmap.query(query_string[0], query_string[1], query_string[2], query_string[3])
