from game_state import GameState
from tic_tac_toe import TicTacToe

print("Welcome to Tic-Tac-Toe...")

"""
TODO: Summary goes here

Returns:
  Did any of the players win, is it a draw, or is the game still ongoing?
"""
def main():
  # RECEIVES USER INPUT TO SELECT THEIR TOKEN (‘X’ OR ‘O’), REMOVING SURROUNDING WHITE SPACE AND CONVERTING THE STRING TO UPPERCASE.
  selected_token = input("Select your token (X or O):").strip().upper()

  if selected_token == 'X' or selected_token == 'O':
      game = TicTacToe(current_player=selected_token)
  else:
      print("Invalid input. Defaulting to 'X'.")
      game = TicTacToe(current_player='X')