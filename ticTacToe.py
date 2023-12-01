
# List to store the 3x3 grid

board = [
  [" "," "," "],
  [" "," "," "],
  [" "," "," "]
]


# Display the board 
def display_board():
   for row in board:
      print("|".join(row))
      print("-----")


# Function for player input
def make_move(player_symbol,position):
    
    # Perform calculations for user input to correpsond with list indexing
    position -= 1 
    row, col = divmod(position, 3) # Returns remainder of position // 3

    if board[row][col] == " ":
        board[row][col] = player_symbol
        return True
    else:
        print("Invalid move. Try again.")
        return False

# Check for wins
def check_win():
  # Check horizontal win
  for row in board:
    if all(cell =="X" for cell in row) or all(cell=="O" for cell in row):
      return True
  # Check columns
  for col in range(3):
     if all(row[col] =="X" for row in board) or all(row[col] == "O" for row in board):
        return True
     
  # Check top-left to bottom-right diagonal
  if all(board[i][i] == "X" for i in range(3)) or all(board[i][i] == "O" for i in range(3)):
     return True
  # Check top-right to bottom-left diagonal
  if all(board[i][2 - i] == "X" for i in range(3)) or all(board[i][2 - i] == "O" for i in range(3)):
    return True

  return False



current_player = "X"

while True:
  display_board()


  #Get player input
  position = (int(input(f"Player {current_player}, enter your move (1-9)")))

  if not(1 <= position <=9):
     print("Invalid input. Please enter a number between 1 and 9.")
     continue

  if make_move(current_player,position):
      if check_win():
        display_board()
        print(f"Player {current_player} wins!")
        break
      elif all(cell !=" " for row in board for cell in row):
         display_board()
         print("It's a draw!")
         break
      else:
         current_player = "O" if current_player == "X" else "X"
         
