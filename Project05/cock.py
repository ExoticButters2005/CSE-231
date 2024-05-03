import csv


filename = "card_data.csv"

try:
    with open(filename, "r", encoding="utf-8") as file:
        
        contents = file.readlines()
        for row in contents:
            print(row)
except FileNotFoundError:
    print(f"Error: The file '{filename}' could not be found.")
except Exception as e:
    print(f"An error occurred: {e}")