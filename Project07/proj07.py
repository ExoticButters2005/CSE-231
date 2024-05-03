"""
def prompt_init_crossword():
 takes in user input for the filename of the crossword puzzle:
  initializes the crossword from filename 
    if the file is not found, print error message   
def display clues
 clues = crossword.clues
 initializes 2 lists for down and accross clues
 in case count = 0, total clues = count
 for indices and respective clue in all clues
  if len clue < count and > 0
    append to respective list
  print clues according to input
def get_and_validate_cmds(param: crossword, input):
 split user input
 user command = first character of input
 remaining option = remaining characters
 while True:
  if command = C and option doesnt exceed 1 character and is > 0:
   retun crossword
  if command in H S Q
   if H print help menu return crossword
   if S print reload crossword print crossword and help menu
   if Q exit the program
  if command in G R T
   if input doesnt match up to 3 characters return none
  if command = G
   	try to turn i and j into  integer index value 
  if command = R
        reveal answer and print crossword
  if command = T
        reveal the position of wrong letter and the correct letter 
def main():
 initialize crossword using prompt_init_crossword()
 print out crossword and help menu
 while true
  ask for user option 
  test and valid date said options
  return the results into a test crossword
  if test crossword is true and not none:
    test crossword becomes crossword
  else if test crossword IS none:
    print error message 
  if crossword is solved
    print congratulations message

skeleton code at the bottom 
"""

from crossword import Crossword
from crossword import Clue
import sys


HELP_MENU = "\nCrossword Puzzler -- Press H at any time to bring up this menu" \
                "\nC n - Display n of the current puzzle's down and across clues" \
                "\nG i j A/D - Make a guess for the clue starting at row i, column j" \
                "\nR i j A/D - Reveal the answer for the clue starting at row i, column j" \
                "\nT i j A/D - Gives a hint (first wrong letter) for the clue starting at row i, column j" \
                "\nH - Display the menu" \
                "\nS - Restart the game" \
                "\nQ - Quit the program"


OPTION_PROMPT = "\nEnter option: "
PUZZLE_PROMPT = "Enter the filename of the puzzle you want to play: "
PUZZLE_FILE_ERROR = "No puzzle found with that filename. Try Again.\n"
"\nAcross"
"\nDown"
"\nPuzzle solved! Congratulations!"
"Letter {} is wrong, it should be {}"
"Invalid option/arguments. Type 'H' for help."
GUESS_PRMPT = "Enter your guess (use _ for blanks): "
"This clue is already correct!"

RuntimeError("Guess length does not match the length of the clue.\n")
RuntimeError("Guess contains invalid characters.\n")

# def input( prompt=None ):
#     """
#         DO NOT MODIFY: Uncomment this function when submitting to Codio
#         or when using the run_file.py to test your code.
#         This function is needed for testing in Codio to echo the input to the output
#         Function to get user input from the standard input (stdin) with an optional prompt.
#         Args:
#             prompt (str, optional): A prompt to display before waiting for input. Defaults to None.
#         Returns:
#             str: The user input received from stdin.
#     """
#
#     if prompt:
#         print( prompt, end="" )
#     aaa_str = sys.stdin.readline()
#     aaa_str = aaa_str.rstrip( "\n" )
#     print( aaa_str )
#     return aaa_str


# DEFINE YOUR FUNCTIONS HERE
crossword = None # global variable to store the crossword object
def prompt_init_crossword():
    
    while True:
        try:
            filename = input(PUZZLE_PROMPT) # asks for filename from user
            crossword = Crossword(filename) # creates a crossword object
            (display_clues(crossword, 0)) # displays clues everytime a new crossword is loaded
            return crossword
        except FileNotFoundError: # in case file not found, print error message
            print(PUZZLE_FILE_ERROR)
    
def display_clues(crossword: Crossword, count = 0):
    clues = crossword.clues 
    across_clues = [] # initialize empty list for across clues
    down_clues = [] #  initialize empty list for down clues
    if count == 0: # if count is 0, display all clues
        count = len(clues)
    
    for coords, clue in clues.items(): # iterate through the clues
        
        if coords[2] == "A" and count > 0 and len(across_clues) < count:  # if the clue is across and the count is greater than 0 and the length of across_clues is less than the count
            across_clues.append(clue)
        if coords[2] == "D" and count > 0 and len(down_clues) < count: # if the clue is down and the count is greater than 0 and the length of down_clues is less than the count
            down_clues.append(clue)
    
    print("\nAcross")
    for clue in across_clues:
        print(clue)
    print("\nDown")
    for clue in down_clues:
        print(clue)
        

        
def get_and_validate_cmds(crossword: Crossword, user_input):
    user_input = user_input.split()
    if len(user_input) < 1:
        return None
    cmd = user_input[0]
    opt = user_input[1:]
    while True:
            if cmd == "C":
                if len(opt) != 1: # if length of user input is not 1, return None
                    return None
                n = int(opt[0]) # convert the input to integer
                if n < 0:
                    return None
                display_clues(crossword, n)
                return crossword
            elif cmd in ["H", "S", "Q"]:
                if cmd == "H":
                    print(HELP_MENU)
                    return crossword 
                    
                elif cmd == "S":
                    crossword = prompt_init_crossword() # upon restart, prints the crossword, help menu 
                    print(crossword.__str__())
                    print(HELP_MENU)
                    return crossword
                elif cmd == "Q":
                    sys.exit(0)
            elif cmd in ["G", "R", "T"]:
                if len(opt) != 3: # if length of input doesn't match up to 3 characters
                    return None
                try:
                    i = int(opt[0])
                    j = int(opt[1])
                except ValueError: # in case of invalid indices,
                    return None
                if i < 0 or j < 0: # also in case invalid indices return None
                    return None
                indice = opt[2]
                if indice not in ["A", "D"]: # also in case of invalid direction, return None
                    return None
                try:
                    clue = crossword.clues[(i, j, indice)]
                except KeyError: # in case of invalid clue, return None
                    return None
                if cmd == "G": # when user wants to make a guess
                    while True:
                        try:
                            guess = input(GUESS_PRMPT).upper() # asks for user guess and converts it to uppercase
                            crossword.change_guess(clue, guess) # changes the guess
                            break
                        except RuntimeError as e: # in case of runtime error, print error message
                            print(e)
                    print(crossword.__str__())
                    return crossword
                if cmd == "R": # when user wants to reveal the answer
                    crossword.reveal_answer(clue)
                    print(crossword.__str__())
                    return crossword
                if cmd == "T": # when user wants a hint
                    if crossword.find_wrong_letter(clue) == -1: # if the clue is already correct
                        print("This clue is already correct!")
                    else:
                        print("Letter {} is wrong, it should be {}".format(crossword.find_wrong_letter(clue) + 1, clue.answer[crossword.find_wrong_letter(clue)]))
                    return crossword
            else: # in case of invalid option, return None
                return None
                
                    

def main():
    crossword = prompt_init_crossword()
    print(crossword)
    print(HELP_MENU)
    while True:
        user_input = input(OPTION_PROMPT)
        test_crossword = get_and_validate_cmds(crossword, user_input) # get and validate commands through a test crossword
        if test_crossword: # in case test crossword isn't none
            crossword = test_crossword # set crossword to dummy crossword
        else:
            print("Invalid option/arguments. Type 'H' for help.")
        if crossword is not None and crossword.is_solved():
            print("\nPuzzle solved! Congratulations!") # if the puzzle is solved, print this message
            break

if __name__ == "__main__":
    main()
