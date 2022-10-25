


from Player_AI import *
from GameBoard import *
from MiniMax import *

import random
import math
import copy



end = False

while not end:

    #Creating original score for both player and AI agent
    player_score = 0
    agent_score = 0

    #Getting started
    board, num_play = game_begin()

    #Building the drawing the original board
    board.board_builder()

    board.board_drawer()

    #Ensuring the game is actually being activated
    game_in_process = True

    while game_in_process:
        #Player making moves
        player_score = player(board, player_score, agent_score, num_play)
        game_in_process = board.remaining_moves()

        if not game_in_process:
            break

        #AI agent making moves
        agent_score = AI_agent(board, agent_score, player_score, num_play)
        game_in_process = board.remaining_moves()

        if not game_in_process:
            break

    # Game completion
    print("Game over.")
    board.board_drawer()

    # Notifying who the winner of the game is, and providing the option to play the game again
    winner(player_score, agent_score)
    play_again = input("\nPlay the game again? \nIf so, press any key, or else press E.")

    if play_again == "E":
        end = True