#!/usr/bin/env python3

class TicTacToe:
    def __init__(self, current_player):
        self.current_player = current_player 

    board = ['?'] * 9 
    current_player = "X"
    winner = None
    game_running = True

    # Prints a 3x3 game board
    def print_board(board):
        row = 0
        while row < 3:
            for col in range(3):
                print("|" + board[row] + "|", end="")
            print("\n---------") if row < 2 else ""
            row += 1 
    print_board(board)


