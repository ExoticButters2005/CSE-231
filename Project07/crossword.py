"""
def change_guess(clue, new_guess):
 if len of guess isn't equal to len of answer:
 raise error
 if guess contains invalid characters 
 also raises error
 initializes row and column values = clue.indices 
 orientation = clue.down_across
 checks if orientation = A or D
  iterate through the len of guess/answer:
    updates the board with new guess according to respective orientation
def reveal_answer(clue):
 call change guess function and updates the guess with correct answer
def get_current_guess(clue):
 similar to change_guess but appends value of current guess on the board 
 corresponding to indices and index values of answer
def find_wrong_letter(clue):
 call get current guess to get current guess
 answer = clue.answer
 for i in range of len guess/answer
  checks for index of each char 
   returns the index of the first mismatched char
 else if all correct return -1

def is_solved():
 for every answer
  call find_wrong_letter function 
  if the value returned is more or equal to 0
   return false
 else:
  return True
"""

import csv

CROSSWORD_DIMENSION = 5

GUESS_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"


class Clue:
    def __init__(self, indices, down_across, answer, clue):
        """
        Puzzle clue constructor
        :param indices: row,column indices of the first letter of the answer
        :param down_across: A for across, D for down
        :param answer: The answer to the clue
        :param clue: The clue description
        """
        self.indices = indices
        self.down_across = down_across
        self.answer = answer
        self.clue = clue

    def __str__(self):
        """
        Return a representation of the clue (does not include the answer)
        :return: String representation of the clue
        """
        return f"{self.indices} {'Across' if self.down_across == 'A' else 'Down'}: {self.clue}"

    def __repr__(self):
        """
        Return a representation of the clue including the answer
        :return: String representation of the clue
        """
        return str(self) + f" --- {self.answer}"

    def __lt__(self, other):
        """
        Returns true if self should come before other in order. Across clues come first,
        and within each group clues are sorted by row index then column index
        :param other: Clue object being compared to self
        :return: True if self comes before other, False otherwise
        """
        return ((self.down_across,) + self.indices) < (
            (other.down_across,) + other.indices
        )


class Crossword:
    def __init__(self, filename):
        """
        Crossword constructor
        :param filename: Name of the csv file to load from. If a file with
        this name cannot be found, a FileNotFoundError will be raised
        """
        self.clues = dict()
        self.board = [
            ["■" for _ in range(CROSSWORD_DIMENSION)]
            for __ in range(CROSSWORD_DIMENSION)
        ]
        self._load(filename)

    def _load(self, filename):
        """
        Load a crossword puzzle from a csv file
        :param filename: Name of the csv file to load from
        """
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                indices = tuple(map(int, (row["Row Index"], row["Column Index"])))
                down_across, answer = row["Down/Across"], row["Answer"]
                clue_description = row["Clue"]
                clue = Clue(indices, down_across, answer, clue_description)

                key = indices + (down_across,)
                self.clues[key] = clue

                i = 0
                while i < len(answer):
                    if down_across == "A":
                        self.board[indices[0]][indices[1] + i] = "_"
                    else:
                        self.board[indices[0] + i][indices[1]] = "_"
                    i += 1

    def __str__(self):
        """
        Return a string representation of the crossword puzzle,
        where the first row and column are labeled with indices
        :return: String representation of the crossword puzzle
        """
        board_str = "     " + "    ".join([str(i) for i in range(CROSSWORD_DIMENSION)])
        board_str += "\n  |" + "-" * (6 * CROSSWORD_DIMENSION - 3) + "\n"
        for i in range(CROSSWORD_DIMENSION):
            board_str += f"{i} |"
            for j in range(CROSSWORD_DIMENSION):
                board_str += f"  {self.board[i][j]}  "
            board_str += "\n"

        return board_str

    def __repr__(self):
        """
        Return a string representation of the crossword puzzle,
        where the first row and column are labeled with indices
        :return: String representation of the crossword puzzle
        """
        
        return str(self)

    def change_guess(self, clue:Clue, new_guess):  
        """
        updates the crossword puzzle with a new guess for a given clue
        :param clue: Clue object representing the clue to be updated
        :param new_guess: The new guess to be added to the crossword puzzle                  
        """
        if len(new_guess) != len(clue.answer): # if guess length does not match the length of the clue
            raise RuntimeError("Guess length does not match the length of the clue.\n")
        
        if not all(ch in GUESS_CHARS for ch in new_guess): # if guess contains invalid characters
            raise RuntimeError("Guess contains invalid characters.\n")
            
        row, col = clue.indices
        orientation = clue.down_across
        if orientation == "A":
            for i in range(len(new_guess)): # iterates through the length of the new guess
                self.board[row][col + i] = new_guess[i] # updates the board with the new guess
        elif orientation == "D":
            for i in range(len(new_guess)): 
                self.board[row + i][col] = new_guess[i]
        

    def reveal_answer(self, clue:Clue):
        """
        Reveals the correct answer for a given clue on the crossword puzzle board
        :param clue: Clue object representing the clue to be revealed
        """
        self.change_guess(clue, clue.answer) # calls change guess function to update the guess with the correct answer
        
    def get_current_guess(self, clue:Clue):
        """
        Gets the current guess of the user for a given clue
        :param clue: Clue object representing the clue to be revealed
        :return: The current guess of the user for the given clue
        """
        guess = ""
        row, col = clue.indices
        orientation = clue.down_across
        if orientation == "A":
            for i in range(len(clue.answer)): # iterates through the length of the answer
                guess += self.board[row][col + i] # adds the letter to the guess
        elif orientation == "D":
            for i in range(len(clue.answer)):
                guess += self.board[row + i][col] 
        return guess
        


    def find_wrong_letter(self, clue:Clue):  
        """
        Points out the first instance where the user's guess diverges
        from the actual answer
        :param clue: Clue object representing the clue to be revealed
        :return: The integer index of the first wrong letter in the user's guess
        """
        guess = self.get_current_guess(clue) # gets the current guess
        answer = clue.answer # gets the answer
        for i in range(len(answer)):
            if guess[i] != answer[i]:
                return (i) # returns the index of the first wrong letter
        return -1 # if the guess is correct, returns -1


    def is_solved(self):  
        """
        Checks whether the entire crossword puzzle has been successfully solved
        :return: True if the crossword puzzle has been solved, False otherwise
        """
        for clues in self.clues.values():
            if self.find_wrong_letter(clues) >= 0: # if find wrong letter returns a positive index
                return False
        return True
