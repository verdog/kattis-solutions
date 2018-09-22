#!/usr/bin/python3

class Square:
    def __init__(self, value):
        self.value = int(value)

    def __str__(self):
        return str(self.value)

class Board:
    def __init__(self):
        self.rows = []
        for i in range(4):
            self.rows.append([Square(0)] * 4)

        self.move_dict = {
            '0': "left",
            '1': "up",
            '2': "right",
            '3': "down"
        }

    def __str__(self):
        string = ""
        for row in self.rows:
            for s in row:
                string += str(s) + ' '
            string += '\n'
        return string

    def build(self):
        for i in range(4):
            line = input()
            numbers = line.split()
            for j in range(4):
                self.rows[i][j] = Square(numbers[j])

    def move(self, direction):
        self.collapse(direction)
        self.combine(direction)
        self.collapse(direction)

    def collapse(self, direction):
        # collapses the board in a direction such that there are no zeros in between anything.
        # DOES NOT combine numbers.

        if self.move_dict[direction] == 'left':
            self.collapse_left()

        if self.move_dict[direction] == 'right':
            self.collapse_right()

        if self.move_dict[direction] == 'up':
            self.collapse_up()

        if self.move_dict[direction] == 'down':
            self.collapse_down()
        
    def collapse_left(self):
        for i in range(len(self.rows)):
            new_sequence = []
            for square in self.rows[i]:
                if square.value != 0:
                    new_sequence.append(Square(square.value))
            while len(new_sequence) != 4:
                new_sequence.append(Square(0))
            self.rows[i] = new_sequence

    def collapse_right(self):
        self.rotate_cw()
        self.rotate_cw()
        self.collapse_left()
        self.rotate_cw()
        self.rotate_cw()

    def collapse_up(self):
        self.rotate_cw()
        self.rotate_cw()
        self.rotate_cw()
        self.collapse_left()
        self.rotate_cw()

    def collapse_down(self):
        self.rotate_cw()
        self.collapse_left()
        self.rotate_cw()
        self.rotate_cw()
        self.rotate_cw()
        
    def rotate_cw(self):
        new_rows = [None] * 4
        for i in range(4):
            new_rows[i] = [Square(0)] * 4

        for i in range(4):
            for j in range(4):
                new_rows[j][i] = self.rows[3-i][j]

        self.rows = new_rows

    def combine(self, direction):
        if self.move_dict[direction] == 'left':
            self.combine_left()

        if self.move_dict[direction] == 'right':
            self.combine_right()

        if self.move_dict[direction] == 'up':
            self.combine_up()

        if self.move_dict[direction] == 'down':
            self.combine_down()

    def combine_left(self):
        # combines like numbers that are next to each other with respect to direction.

        for i in range(len(self.rows)):
            for j in range(3):
                square_first = self.rows[i][j]
                square_second = self.rows[i][j+1]
                if square_first.value == square_second.value:
                    square_first.value *= 2
                    square_second.value = 0

    def combine_right(self):
        self.rotate_cw()
        self.rotate_cw()
        self.combine_left()
        self.rotate_cw()
        self.rotate_cw()

    def combine_up(self):
        self.rotate_cw()
        self.rotate_cw()
        self.rotate_cw()
        self.combine_left()
        self.rotate_cw()

    def combine_down(self):
        self.rotate_cw()
        self.combine_left()
        self.rotate_cw()
        self.rotate_cw()
        self.rotate_cw()
                    
                

board = Board()
board.build()

move = input()

board.move(move)
print(board)
