#!/usr/bin/env python3
# FIXME: resolve import issues
from models.game_state import GameState

class TicTacToe:
    def __init__(self, current_player):
        self.current_player = current_player 
        self.board = ['?' for _ in range(10)]
        self.winner = None
        self.game_state = GameState.ONGOING

    # PRINTS A 3X3 GAME BOARD
    def print_board(board):
        row = 0
        while row < 3:
            for col in range(3):
                print("|" + board[row] + "|", end="")
            print("\n---------") if row < 2 else ""
            row += 1 
    print_board(board)


    # TAKES USER INPUT TO SELECT A CELL AND CHECK IF IT'S ALREADY TAKEN
    def check_cell(board, row, col):
        selected_index = row * 3 + col
        selected_cell = board[selected_index]

        # TODO: validate selection
        if selected_cell != '?': 
            return False 
        return True

    # CHECKS IF SELECTED CELL IS TAKEN AND PLACES TOKEN
    def place_token(board, current_player):
        while True:
            print_board(board)
            try:
                row, col = map(int(input("Select a row and column to place a token: ")).split())

                # Validating the token placement selection
                if 0 <= row < 3 and 0 <= col < 3:
                    selected_index = row * 3 + col
                    # Exits loop when valid selection is made
                    if check_cell(board, row, col):
                        board[selected_index] = current_player
                        return  
                    else:
                        print("That cell is already taken. Try again.")
                else:
                    print("Invalid row or column. Try again.")

            except ValueError:
                print("Invalid input; please try again.")

            
    
