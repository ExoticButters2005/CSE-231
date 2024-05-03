###########################################################
#  """
# def prompt_init_crossword():
#  takes in user input for the filename of the crossword puzzle:
#   initializes the crossword from filename 
#     if the file is not found, print error message   
# def display clues
#  clues = crossword.clues
#  initializes 2 lists for down and accross clues
#  in case count = 0, total clues = count
#  for indices and respective clue in all clues
#   if len clue < count and > 0
#     append to respective list
#   print clues according to input
# def get_and_validate_cmds(param: crossword, input):
#  split user input
#  user command = first character of input
###########################################################
from force import ForceCalculator
import sys

MENU = '''\n:~Net Force Calculator Program
          1) Add force
          2) Remove force
          3) Show forces
          4) Find force components
          5) Compute resultant force
          6) Reset calculator
          7) Stop the program
          Enter option~:'''

":~\nEnter value for {}~:"
"\nInput {} is not a valid float number!"
":~\nEnter name of force~:"
"Magnitude (N)"
"Angle (degrees)"
"\nForce objects in the calculator"
"\nThere are no force objects in the calculator."

"\nForce components for Force object {}:"
"\nMagnitude: {}"
"\nFx = {}"
"\nFy = {}"

"\nResultant force of all forces in the calculator"

"\nInvalid option. Please Try Again!"





def prompt_num(prompt):
    """
    I LOVE POKEMON GO
    I LOVE POKEMON GO
    I LOVE POKEMON GO
    I LOVE POKEMON GO
    I LOVE POKEMON GO
    """
    while True:
        user_input = (input(prompt))
        try:
            user_input = float(user_input)
            return user_input   
        except ValueError:
            print(f"\nInput {user_input} is not a valid float number!")

def main():
    calculator = ForceCalculator()
    while True:
        choice = input(MENU)
        if choice == "1":
            name = input("\n:~Enter name of force~:")
            magnitude = prompt_num("\n:~Enter value for Magnitude (N)~:")
            angle = prompt_num("\n:~Enter value for Angle (degrees)~:")
            try:
                calculator.add_force(name, magnitude, angle)
            except RuntimeError as e:
                print(e)
        elif choice == "2":
            name = input("\n:~Enter name of force~:")
            try:
                calculator.remove_force(name)
            except RuntimeError as e:
                print(e)
        elif choice == "3":
            if len(calculator.forces) == 0:
                print("\nThere are no force objects in the calculator.")
            else:
                print("\nForce objects in the calculator")
                print(calculator)
                
        elif choice == "4":
            name = input("\n:~Enter name of force~:")
            if name in calculator.forces:
                force = calculator.forces[name]
                x, y = force.get_components()
                print(f"\nFx = {x}")
                print(f"\nFy = {y}")
            else:
                print(f"\nForce object {name} does not exist!")
        elif choice == "5":
            result = calculator.compute_net_force()
            print(
                f"\nResultant force of all forces "
                f"in the calculator\n{result}")
        elif choice == "6":
            calculator = ForceCalculator()
            print("Calculator reset.")
        elif choice == "7":
            
            break
        else:
            print("\nInvalid option. Please Try Again!")

if __name__ == "__main__":
    main()

