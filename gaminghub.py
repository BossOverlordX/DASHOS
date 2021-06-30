# Copyright (c) 2021, Dashiell Ratcliffe
# All rights reserved.
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. 

def Gaminghub(currentdir):
  os.system('cls' if os.name == 'nt' else 'clear')
  print(colored("""

           ___                _                            _     
          / _ \__ _ _ __ ___ (_)_ __   __ _    /\  /\_   _| |__  
 ________/ /_\/ _` | '_ ` _ \| | '_ \ / _` |  / /_/ / | | | '_ \________
|       / /_\\\ (_| | | | | | | | | | | (_| | / __  /| |_| | |_) |       |
|       \____/\__,_|_| |_| |_|_|_| |_|\__, | \/ /_/  \__,_|_.__/        |
|                                     |___/                             |""", "magenta", attrs=["bold"]), colored("""
|                                                                       |
|    ┌─────┬──────┬─────┐  ┌──────────────────┐  ┌──────────────────┐   |
|    │     │      │     │  │                  │  │ M          6     │   |
|    │  T  │  I   │  C  │  │  H ┌─────────┐   │  │                  │   |
|    │     │      │     │  │  A │         │   │  │  E   1        9  │   |
|    ├─────┼──────┼─────┤  │  N │         │   │  │                  │   |
|    │     │      │     │  │  G │        ( )  │  │   M     3        │   |
|    │  T  │  A   │  C  │  │  M │        /|\  │  │                  │   |
|    │     │      │     │  │  A │        / \  │  │    O        4    │   |
|    ├─────┼──────┼─────┤  │  N │             │  │                  │   |
|    │     │      │     │  │    │             │  │     R   7        │   |
|    │  T  │  O   │  E  │  │ ───┴───          │  │             8    │   |
|    │     │      │     │  │                  │  │      Y           │   |
|    └─────┴──────┴─────┘  └──────────────────┘  └──────────────────┘   |
|                                                                       |
|_______________________________________________________________________|
""", "blue", attrs=["bold"]))
  q = False
  while q == False:
    time.sleep(0.5)
    # Ask user for game to play or quit
    game = input(colored("\nPlease select a game: ", "blue"))
    if game.lower() == "quit":
      os.system('cls' if os.name == 'nt' else 'clear')
      Cmdline(logincurrentuser, currentdir)
    elif game.lower() == "tictactoe":
      TicTacToe(currentdir)
    elif game.lower() == "hangman":
      Hangman(currentdir)
    elif game.lower() == "memory":
      Memory(currentdir)
    else:
      print("Game not found ('quit' returns to CLI)")

def Memory(currentdir):
  os.system('cls' if os.name == 'nt' else 'clear')
  # Easy difficulty
  def Easy(level):
    nums = []
    # Number of numbers to memorise directly proportional to level number
    for i in range(0,level+1):
      nums.append(random.randint(0,9))
    # Tell user their level num
    line = "".join(map(str, nums))
    print(f"This is level {level} on difficulty easy")
    time.sleep(0.5)
    print("Memorise the following line:\n")
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    # Print numbers to memorise one by one
    for i in range(0, len(nums)):
      time.sleep(1)
      print(line[i])
    time.sleep(1)
    # Clear terminal and get user to input what they remember
    os.system('cls' if os.name == 'nt' else 'clear')
    answer = input("Enter the numbers you just saw with no spaces: ")
    # If they were right and were on the last level, they beat easy mode!
    if answer == line and level == 6:
      print("Congrats! You completed Easy Mode!!!")
      time.sleep(1)
      Gaminghub(currentdir)
    # If they were right but not on the last level, restart the function with level + 1
    if answer == line:
      print(f"Congrats! You completed level {level}")
      Easy(level+1)
    # If they were wrong, tell them what the correct combo was before going back to gaminghub
    else:
      print(f"Oh no! You failed :(\nThe correct combo was {line}")
      time.sleep(4)
      Gaminghub(currentdir)
  # Medium difficulty
  def Medium(level):
    nums = []
    for i in range(0,level+1):
      nums.append(random.randint(0,9))
    line = "".join(map(str, nums))
    print(f"This is level {level} on difficulty medium")
    time.sleep(0.5)
    print("Memorise the following line:\n")
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(0, len(nums)):
      time.sleep(0.8)
      print(line[i])
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    answer = input("Enter the numbers you just saw with no spaces: ")
    if answer == line and level == 8:
      print("Congrats! You completed Medium Mode!!!")
      time.sleep(1)
      Gaminghub(currentdir)
    if answer == line:
      print(f"Congrats! You completed level {level}")
      Medium(level+1)
    else:
      print(f"Oh no! You failed :(\nThe correct combo was {line}")
      time.sleep(2)
      Gaminghub(currentdir)
  # Hard difficulty
  def Hard(level):
    nums = []
    for i in range(0,level+1):
      nums.append(random.randint(0,9))
    line = "".join(map(str, nums))
    print(f"This is level {level} on difficulty hard")
    time.sleep(0.5)
    print("Memorise the following line:\n")
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(0, len(nums)):
      time.sleep(0.7)
      print(line[i])
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    answer = input("Enter the numbers you just saw with no spaces: ")
    if answer == line and level == 10:
      print("Congrats! You completed Hard Mode!!!")
      time.sleep(1)
      exit()
    if answer == line:
      print(f"Congrats! You completed level {level}")
      Hard(level+1)
    else:
      print(f"Oh no! You failed :(\nThe correct combo was {line}")
      time.sleep(2)
      Gaminghub(currentdir)


  print("Welcome to the Memory Game!")
  print("Memorise the numbers to advance and complete the levels")
  time.sleep(1)
  q = False
  # Ask to input difficulty until valid number is entered
  while q == False:
    try:
      difficulty = int(input("Difficulty (1,2,3): "))
    except:
      print("Enter a number")
      time.sleep(1)
      Memory(currentdir)
    if difficulty == 1:
      # Play easy level 0
      Easy(0)
    elif difficulty == 2:
      # Play medium level 0
      Medium(0)
    elif difficulty == 3:
      # Play hard level 0
      Hard(0)
    else:
      print("Please enter a valid difficulty")

def Hangman(currentdir):
  os.system('cls' if os.name == 'nt' else 'clear')
  cprint("""
     _____
    |     |
    |     0
    |    /|\\
    |    / \\
    |
  __|__

  """, "red")
  print("Welcome to Hangman!")
  time.sleep(1)
  print("You will have 10 guesses\n")
  time.sleep(0.5)
  # All possible words
  wordlist = ["epicalyx","pawn","active","baseball","discrimination","tire","still","buy","carbon","middle","divide","designer","body","actor","spider","bare","priority","science","activity","sacred","dirty","confusion","sunshine","regular","receipt","fish","tolerant","distant","tasty","tiptoe","training","entry","fragment","glimpse","publish","negligence","flourish","decrease","inner","labour","grain","illustrate","zone","marine","trust","adviser","answer","post","clean"]
  # Choose a random word to be the hangman word
  word = random.choice(wordlist)
  goes = ('')
  turns = 10
  # While they haven't run out of turns
  while turns > 0:         
    failed = 0
    for char in word:
      # If a previously guessed letter is in the word, print it out
      if char in goes:    
        print("", char, end="")
      # If a letter is not previously guessed, print an underscore and failed != 0
      else:
        print(" _", end="")
        failed += 1   
    # If they have got all letters of the word, they win! 
    if failed == 0:        
      print("\nYou win!")
      time.sleep(2)
      Gaminghub(currentdir)
    print()
    # Ask user for what letter they want to try
    letter = input("\nLetter: ") 
    # Add the letter to goes
    goes += letter
    # If the letter was not in the word, tell the user how many more guesses
    if letter not in word:  
      turns -= 1        
      print("\nWrong\n")
      print("You have", turns, 'more guesses')
      # If the user has run out of turns, they lose, tell them the word
      if turns == 0:
        print("\nYou Lose")
        print("The word was", word)
        time.sleep(2.5)
        Gaminghub(currentdir)

def TicTacToe(currentdir):
  os.system('cls' if os.name == 'nt' else 'clear')
  # Board is stored as list
  global board1
  global board2
  global board3
  board1 = [" "," "," "]
  board2 = [" "," "," "]
  board3 = [" "," "," "]
  # On both turns, print out board and ask user to input their space
  def Turn():
    print(f"\n|{board1[0]}|{board1[1]}|{board1[2]}|")
    print(f"|{board2[0]}|{board2[1]}|{board2[2]}|")
    print(f"|{board3[0]}|{board3[1]}|{board3[2]}|")
    try:
      num = int(input("P1: (1-9) "))
    except:
      print("Please enter a number")
      Turn()
    # Add mark on board with corresponding symbol
    Addmark(num, "X")

  def Turn2():
    print(f"\n|{board1[0]}|{board1[1]}|{board1[2]}|")
    print(f"|{board2[0]}|{board2[1]}|{board2[2]}|")
    print(f"|{board3[0]}|{board3[1]}|{board3[2]}|")
    try:
      num = int(input("P2: (1-9) "))
    except:
      print("Please enter a number")
      Turn2()
    Addmark(num, "O")
  # Adding a nought or cross
  def Addmark(num, userturn):
    # If num < 4 add mark to board 1
    if num < 4:
      # Number -= 1 as computers count from 0
      num -= 1
      # If space is clear
      if board1[num] == " ":
        board1[num] = userturn
      # Otherwise, not a valid option
      else:
        Validnum(userturn)
    # If not then if num < 7 add mark to board 2
    elif num < 7:
      # number -= 1 as computers count from 0 and board 2 starts at 4
      num -= 4
      # If space is clear
      if board2[num] == " ":
        board2[num] = userturn
      # Otherwise, not a valid option
      else:
        Validnum(userturn)
    # If not then if num < 10 add mark to board 3
    elif num < 10:
      # number -= 1 as computers count from 0 and board 3 starts at 7
      num -= 7
      # If space is clear
      if board3[num] == " ":
        board3[num] = userturn
      # Otherwise, not a valid option
      else:
        Validnum(userturn)
    # Otherwise number is not valid
    else:
      Validnum(userturn)
    # Once mark has been added, check for a win
    Wincheck(userturn)

  def Validnum(userturn):
    # Repeat the user turn carrying over the mark symbol
    print("Please enter a valid number")
    try:
      num = int(input("(1-9) "))
    except:
      Validnum(userturn)
    Addmark(num, userturn)

  # Check if win condition met
  def Wincheck(userturn):
    # Check for horizontal win
    if (board1[0] == userturn and board1[1] == userturn and board1[2] == userturn) or (board2[0] == userturn and board2[1] == userturn and board2[2] == userturn) or (board3[0] == userturn and board3[1] == userturn and board3[2] == userturn):
      Win(userturn)
    # Check for vertical win
    if (board1[0] == userturn and board2[0] == userturn and board3[0] == userturn) or (board1[1] == userturn and board2[1] == userturn and board3[1] == userturn) or (board1[2] == userturn and board2[2] == userturn and board3[2] == userturn):
      Win(userturn)
    # Check for diagonal win
    if (board1[0] == userturn and board2[1] == userturn and board3[2] == userturn) or (board1[2] == userturn and board2[1] == userturn and board3[0] == userturn):
      Win(userturn)
    # Check for draw
    if board1[0] != " " and board1[1] != " " and board1[2] != " " and board2[0] != " " and board2[1] != " " and board2[2] != " " and board3[0] != " " and board3[1] != " " and board3[2] != " ":
      print("\nDraw!")
      time.sleep(2)
      Gaminghub(currentdir)
    # If no win, go to next user turn
    if userturn == "X":
      Turn2()
    Turn()

  # Tell users who has one
  def Win(userturn):
    if userturn == "X":
      print("Player 1 Wins!")
    else:
      print("Player 2 Wins!")
    time.sleep(2)
    Gaminghub(currentdir)

  print("\nWelcome to Tic-Tac-Toe!")
  Turn()

#Import all variables and functions from main.py
from __main__ import *
import __main__
Gaminghub("DASHOS/Accounts/Account0")