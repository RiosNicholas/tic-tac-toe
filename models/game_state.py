#!/usr/bin/env python3
from enum import Enum

class GameState(Enum):
    DRAW = 0
    PLAYER_X_WON = 1
    PLAYER_O_WON = 2
    ONGOING = 3
    # INVALID = 4


# CHECKS HORIZONTALLY, VERTICALLY, AND DIAGONALLY FOR WINS IN A 3X3 BOARD
def check_if_won(board, player):
    # Check rows
    for row in range(3):
        if all(board[row * 3 + col] == player for col in range(3)):
            return True
            
    # Check columns
    for col in range(3):
        if all(board[col * 3 + row] == player for row in range(3)):
            return True
            
    # Check diagonally from the top left to bottom right
    if all(board[cell * 3 + cell] == player for cell in range(3)):
        return True

    # Check diagonallly from bottom left to top right
    if all(board[cell * 3 + 2 - cell] == player for cell in range(3)):
        return True

    return False


# CHECKS IF THE GAME IS A DRAW IF THE BOARD IS FILLED AND NO PLAYER HAS WON. 
def check_if_draw():
    return all(cell != '?' for cell in board) and not check_if_won(board)


# CHECKS IF THE GAME IS ONGOING IF NEITHER
def check_if_ongoing():
    is_draw = check_if_draw(board)
    is_win_for_x = check_win(board, 'X')
    is_win_for_o = check_win(board, 'O')

    return not is_draw and not is_win_for_x and not is_win_for_o


def check_game_state():
    try:
        if check_if_won(board, current_player):
            return GameState.PLAYER_X_WON if current_player == 'X' else GameState.PLAYER_O_WON
        elif check_draw(board):
            return GameState.DRAW
        elif check_if_ongoing(board):
            return GameState.ONGOING
        else:
            raise ValueError("Error: An expected game state has occurred.")
    except Exception as e:
        print(f"An error occurred: {e}")
    