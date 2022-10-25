

from GameBoard import *

import random
import math
import copy




#Minimax function
def minimax_func(curr_state, max_num_play):
    optimal_move = []

    state_temporary = copy.deepcopy(curr_state)

    #Searching the optimal move
    value, optimal_move = max_func(state_temporary, max_num_play, 1, None, -math.inf, math.inf, 0)

    return optimal_move


#Maximum function
def max_func(board, max_num_play, curr_play, child, curr_sum, alpha, beta):
    score_max = -math.inf
    move = child

    #Keep tracking of any remaining move to be made, and update current total sum and child
    if not board.remaining_moves():
        return curr_sum, child

    if curr_play > max_num_play:
        state_temporary = copy.deepcopy(board)
        score_max = curr_sum
        return score_max, child

    #Get children given current board position
    children = board.children_finder()

    for child in children:
        # Ensuring the move is not but the child is there
        if move == None and not child == None:
            move = child

        state_temporary = copy.deepcopy(board)
        score_temporary = state_temporary.move(child[0], child[1])

        # Updating the current total sum
        new_curr_sum = curr_sum + score_temporary

        #Using minimum function to return the score
        output, action = mini_func(state_temporary, max_num_play, curr_play + 1, child, alpha, beta, new_curr_sum)

        #Comparing output score with the maximum score, and update
        if (output) > score_max:
            score_max = (output)
            move = child

            #Compare alpa and beta with maximum score
            if alpha < score_max:
                alpha = score_max

        if score_max >= beta:
            return score_max, move

    return score_max, move

#Minmum function
def mini_func(board, curr_play, max_num_play, child, alpha, beta, curr_sum):
    score_min = math.inf
    move = child

    # Keep tracking of any remaining move to be made, and update current total sum and child
    if not board.remaining_moves():
        return curr_sum, child

    if curr_play > max_num_play:
        state_temporary = copy.deepcopy(board)

        score_min = curr_sum

        return score_min, child

    #Get children given current board position
    children = board.children_finder()

    for child in children:
        state_temporary = copy.deepcopy(board)
        score_temporary = state_temporary.move(child[0], child[1])

        # Updating the current total sum
        new_curr_sum = curr_sum - score_temporary

        # Using maximum function to return the score
        output, action = max_func(state_temporary, max_num_play, curr_play + 1, child, alpha, beta, new_curr_sum)

        # Comparing output score with the maminum score, and update
        if (output) < score_min:
            score_min = (output)
            move = child

            # Compare alpa and beta with minimum score
            if beta > score_min:
                beta = score_min

        if score_min <= alpha:
            return score_min, move

    return score_min, move