from random import randint, choice
from replit import clear
from time import sleep

# We will save the board values here.
li = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# restart the game when it's over? the defult is true.
restart_game = True


# choice randomly 'X' or 'O'
# If you are the 'X', you will start first
def choice_sign():
  tic_or_tac = ['X', 'O']
  sign_idx = randint(0, 1)
  your_sign = tic_or_tac[sign_idx]
  if your_sign == 'X':
    your_turn = True
    print(f"Your sign is {your_sign}, you will start fisrt")
  else:
    print(f"Your sign is {your_sign}, the computer will start first")
  return your_sign, tic_or_tac[1 - sign_idx], your_turn


def print_board():
  global li
  board = f' {li[0]} | {li[1]} | {li[2]} \n' \
          f'-----------\n' \
          f' {li[3]} | {li[4]} | {li[5]} \n' \
          f'-----------\n' \
          f' {li[6]} | {li[7]} | {li[8]} \n'
  print(board)


# Here we ask the plyer if he want another game.
# If no, we update the global variable to stop the loop
def another_round():
  global restart_game, li
  # reset the li
  li = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
  if input("Another game? (yes/no)") == "no":
    restart_game = False
  else:
    clear()


def is_full():
  return li.count('X') + li.count('O') == 9


def there_winner():
  # check the col
  for i in range(0, 3):
    if li[i] == li[i + 3] and li[i] == li[i + 6]:
      return True
  # check the rows
  for i in [0, 3, 6]:
    if li[i] == li[i + 1] and li[i] == li[i + 2]:
      return True
  # check the dig
  if li[0] == li[4] and li[0] == li[8] or li[6] == li[4] and li[6] == li[2]:
    return True


def play(your_sign, computer_sign, your_turn):
  turn = your_turn
  computer_idx_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  while not is_full():
    if turn:
      cell_idx = int(input("choose a cell: "))
      while cell_idx not in computer_idx_choices:
        cell_idx = int(input("This cell is not empty. Please choose another cell: "))
      li[cell_idx - 1] = your_sign
    else:
      print("Computer turn")
      sleep(1)
      cell_idx = choice(computer_idx_choices)
      li[cell_idx - 1] = computer_sign
    # remove the cell_idx from computer choices
    computer_idx_choices.remove(cell_idx)
    print_board()

    if there_winner():
      if turn:
        print("You won!")
        return
      else:
        print("You lose :(")
        return
    next_turn = not turn
    turn = next_turn


while restart_game:
  print_board()
  your_sign, computer_sign, your_turn = choice_sign()
  play(your_sign, computer_sign, your_turn)
  # ask if the player want to play another round
  another_round()
