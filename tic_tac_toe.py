from game_state import GameState

class TicTacToe:
    def __init__(self, current_player):
        self.current_player = current_player 
        self.opposite_player = 'O' if current_player == 'X' else 'X'
        self.board = ['?' for _ in range(10)]
        self.winner = None
        self.game_state = GameState.ONGOING

    
    # SWITCHES CURRENT PLAYER AFTER EACH TURN
    def switch_player(self):
        self.current_player, self.opposite_player = self.opposite_player, self.current_player


    # PRINTS A 3X3 GAME BOARD
    def print_board(self):
        row = 0
        while row < 3:
            for col in range(3):
                print("|" + self.board[row] + "|", end="")
            print("\n---------") if row < 2 else ""
            row += 1 
        print("\n")


    # TAKES USER INPUT TO SELECT A CELL AND CHECK IF IT'S ALREADY TAKEN
    def check_cell(self, row, col):
        selected_index = row * 3 + col
        selected_cell = self.board[selected_index]

        if selected_cell != '?': 
            return False 
        return True


    # CHECKS IF SELECTED CELL IS TAKEN AND PLACES TOKEN
    def place_token(self, current_player):
        while True:
            try:
                # Takes user input in the format "row,col", extracts the values after removing whitespace
                row, col = map(int(input("Select a row and column to place a token (row, col):")).replace(" ", "").split(","))

                # Validating the token placement selection
                if 0 <= row < 3 and 0 <= col < 3:
                    selected_index = row * 3 + col
                    # Exits loop when valid selection is made
                    if self.check_cell(board, row, col):
                        self.board[selected_index] = current_player
                        # Print updated board
                        self.print_board()
                        return  
                    else:
                        print("That cell is already taken. Try again.")
                else:
                    print("Invalid row or column. Try again.")

            except ValueError:
                print("Invalid input; please try again.")

            
    
