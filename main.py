from game_state import GameState
from tic_tac_toe import TicTacToe

print("Welcome to Tic-Tac-Toe...")

"""
Handles the main game loop:
    - Selects the player's game token ('X' or 'O'), removing surrounding white space and converting to uppercase.
    - Runs the game loop to keep the game running.
    - Prints the final state of the board and the game outcome.

Returns:
  Did any of the players win, is it a draw, or is the game still ongoing?
"""
def main():
    # SELECTS GAME TOKEN (‘X’ OR ‘O’), REMOVING SURROUNDING WHITE SPACE AND CONVERTING THE STRING TO UPPERCASE.
    selected_token = input("Select your token (X or O):").strip().upper()

    if selected_token == 'X' or selected_token == 'O':
        game = TicTacToe(current_player=selected_token)
    else:
        print("Invalid input. Defaulting to 'X'.")
        game = TicTacToe(current_player='X')


    # MAIN LOOP TO KEEP GAME RUNNING
    while game.game_state == GameState.ONGOING:
        # Prints the current state of the board
        game.print_board()
        
        # Takes user input, validates the selection, and place token
        game.place_token(game.current_player)
        
        # Checks the game state for win or draw after token is placed
        game.game_state = check_game_state(game.board, game.current_player)

        # Switches current player for the next turn
        game.switch_player()
        # Prints the final state of the board once the game is terminated 
        game.print_board()
        

        # OUTPUTS THE FINAL GAME STATE
        if game.game_state == GameState.DRAW:
            return "draw"
        elif game.game_state == GameState.PLAYER_X_WON:
            return "Player X"
        elif game.game_state == GameState.PLAYER_O_WON:
            return "Player O"


if __name__ == "__main__": 
    final_outcome = main()
    print("👾 GAME OVER 👾")
    if final_outcome == "draw":
        print("It's a draw!")
    else:
        print(f"{final_outcome} has won!")