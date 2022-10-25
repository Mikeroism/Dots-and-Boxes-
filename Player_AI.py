

from GameBoard import *
from MiniMax import *


import random
import math
import copy


# Setting up the player attribute
def player(board, player_score, agent_score, max_num_play):
    valid_move = False
    while not valid_move:
        row_num = input("Enter the row number:")
        column_num = input("Enter the column number:")

        if row_num.isnumeric() and column_num.isnumeric():
            row_num = int(row_num)
            column_num = int(column_num)

        if isinstance(row_num, int) or isinstance(column_num, int):
            if board.move_is_valid(column_num, row_num):
                player_score = player_score + board.move(column_num, row_num)
                board.board_drawer()
                print("Player just made a move.")
                print("Latest scores: \nPlayer: {} \nAgent: {}".format(player_score, agent_score))
                valid_move = True
            else:
                print("Try again.")
        else:
                print("Try again.")
    return player_score


# Setting up the AI agent attribute
def AI_agent(board, player_score, agent_score, max_num_play):
    moves = minimax_func(board, max_num_play)
    print("Agent move:", moves)

    agent_score = agent_score + board.move(moves[0], moves[1])
    board.board_drawer()
    print("Agent just made a move.")
    print("Latest scores: \nPlayer: {} \nAgent: {} ".format(player_score, agent_score))

    return agent_score

# Determine who is the winner of the game: player or agent
def winner(player_score, agent_score):
    if player_score > agent_score:
            print("Player won.")
    elif player_score < agent_score:
            print("Agent won.")
    else:
            print("Even match between player and agent.")


# Setting up the process of the game
def game_begin():


# Initializing number of plays
    num_play = 0

    row = int(input("Enter the number of row:"))
    column = int(input("Enter the number of column:"))

# The minimum number of plays needs to be 2
    while num_play < 2:
        num_play = int(input("Enter the maximum number of plays by agent: "))
        if num_play < 2:
                print("Try again.")

    game = Board(row, column, None)
    return game, num_play