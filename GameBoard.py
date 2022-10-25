


import random
import math
import copy


class Board:
    # Initialization of the board class attributes
    def __init__(self, row, column, state):
        self.row = (row*2) + 1
        self.column = (column*2) + 1
        state = state
        self.boxes = (row) * (column)

    # Building the board given the number of rows and columns
    # Ensuring the number of each box is between 1 to 5
    # Marking the intersections with *
    def board_builder(self):

        self.state = []

        for i in range(0, self.row):
            tmp = []
            for j in range(0, self.column):
                if i % 2 == 1 and j % 2 == 1:
                    tmp.append(random.randint(1, 5))
                elif i % 2 == 0 and j % 2 == 0:
                    tmp.append("*")
                else:
                    tmp.append(" ")
            self.state.append(tmp)

    # Drawing the board
    def board_drawer(self):
        print("  ", end = "")
        for i in range(0, self.column):
            print(str(i), end = "  ")
        print()

        for j in range(self.row):
            print(str(j) + "| ", end = "")

            for l in range(self.column):
                print(str(self.state[j][l]), end ="  ")
            print()
        print("  ", end ="")

    # Updating the score if needed when both the player and the AI have completed a box
    def score_updater(self, col, ro):
        score = 0
        # Check if the box is being completed above the bottom of the board
        if self.state[ro][col] == "-":
            if ro <= self.row - 2:
                if self.state[ro + 2][col] == "-" and self.state[ro + 1][col + 1] == "|" and self.state[ro + 1][col - 1] == "|":
                    score = score + self.state[ro + 1][col]

        # Check if the box is being completed below
                if ro > 0:
                    if self.state[ro - 2][col] == "-" and self.state[ro - 1][col + 1] == "|" and self.state[ro - 1][col - 1] == "|":
                        score = score + self.state[ro - 1][col]

        # Check if the box is being completed without going beyond the rightmost edge
        if self.state[ro][col] == "|":
            if col <= self.column - 2:
                if self.state[ro][col + 2] == "|" and self.state[ro + 1][col + 1] == "-" and self.state[ro - 1][col + 1] == "-":
                    score = score + self.state[ro][col + 1]
        # Check if the box is being completed without going beyond the leftmost edge
                if col >= 2:
                    if self.state[ro][col - 2] == "|" and self.state[ro + 1][col - 1] == "-" and self.state[ro - 1][col - 1] == "-":
                        score = score + self.state[ro][col - 1]
        return score

    # Updating player moves and scores
    def move(self, col, ro):
        score = 0
        if col % 2 == 1 and ro % 2 == 0:
            self.state[ro][col] = "-"
        elif col % 2 == 0 and ro % 2 == 1:
            self.state[ro][col] = "|"

        score = self.score_updater(col, ro)

        return score

    # Ensuring the move being completed is valid
    def move_is_valid(self, col, ro):
        # Checking if the move does not reach * or point number
        if col % 2 == 1 and ro % 2 == 1:
            return False
        if col % 2 == 0 and ro % 2 == 0:
            return False

        # Checking the move is within boundary
        if col > self.column or col < 0:
            return False
        if ro > self.row or ro < 0:
            return False

        # Double check to make sure the move has not been done before
        if self.state[ro][col] == "-" or self.state[ro][col] == "|":
            return False

        return True

    def remaining_moves(self):
        for i in range(self.row):
            for j in range(self.column):
                if self.state[i][j] == " ":
                    return True
        return False

    def children_finder(self):
        children = []
        for i in range(self.row):
            for j in range(self.column):
                if self.move_is_valid(j, i):
                    children.append([j, i])
        return children