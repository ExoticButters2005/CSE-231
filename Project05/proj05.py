########################################################################################################################
#
# PROJECT HEADER HERE
# a)
# open_file
# while true
# 	takes in input as file pointer 
#         attempts to open file using try
#         if success returns file pointer
#         except fail then shows fail message and continue
# b) 
# read_card_data
# reads file pointer and extract data 
# initializes card_data list 
# for every line in the dataset:
#  append each element
#  name(limited to 45 char)
#  convert price to float
# sort the final list and returns the final list
# c) OPTION 2
# search_cards
# takes in card_data from read card function
# initialize result list 
# choose category based on input and return that index, category
# compares query to said category
# for card in card_data
#  for query in card[category] 
#    if match, append result, price first then name
# return result list 
# d) OPTION 3 
# read_decklist
# initializes ids list
# initializes deck_list list
# takes in card_data from read card function
# takes in deck list file returned from the openfile func
# takes in the ID of all cards in a deck converting to lists of strings
# for every card in card_data
#  for every id in ids
#   matches them with corresponding card ids in card_data
# append matching cards to deck_list
# sort deck_list by price, ascending then by name
# e) 
# compute_stats
# initializes
# cards with min price, max price and median as lists
# takes in card_data 
# calculates min,max and med price
#     min_price = min(prices)
#     max_price = max(prices)
#     median_price = sorted(prices)[len(prices) // 2]
# search for cards with matching prices
# returns cards with min price, min price
#         cards with max price, max price
#         cards with median price, median price 
# all should be sorted by name 
# f) 
# display_data
# takes in card_data from read card function
# prints the header
# for every card in card_data
#  prints the card data
# prints the total price


# g) OPTION 1
# display_stats
# takes in min_cards, min_price, max_cards, max_price, median_cards, median_price
# prints the min price and the cards with min price
# prints the max price and the cards with max price
# prints the median price and the cards with median price


# prints output from compute_stats function
# h)
# main
 # prompts input for file name
 # reads the file and parse the data
    # while true
    # prompts for option
    # if option 1
    #  display data for cheapest 50 cards
    #  display stats for all cards
    # continue
    # if option 2
    #  search cards
    #  checks for numbers of cards found
     # if empty return no cards found message
     # if not display data and numbers of cards
    # continue
    # if option 3
    #  try to read decklist
    #   display data
    #   display stats
    # except file not found
    #  show error message
    # continue
    # if option 4
    #  break
    # else
    #  invalid option
    # continue
# close the file
# print thank you message
    
 




#
########################################################################################################################


import csv
from operator import itemgetter

# Strings
"\nFile not Found. Please try again!"

"{'Name'}{'Type'}{'Race'}{'Archetype'}{'TCGPlayer'}"
"{}{}{}{}{}"
"\n{'Totals'}{''}{''}{''}{}"

"\nThe price of the least expensive card(s) is {}"
"\nThe price of the most expensive card(s) is {}"
"\nThe price of the median card(s) is {}"
"\t{}" #display the cards after the search

"\nInvalid option. Please try again!"
prompt_str = "\nEnter cards file name: "
"\nThere are {} cards in the dataset."
"\nEnter query: "
"\nEnter category to search: "
"\nIncorrect category was selected!"
"\nSearch results"
"\nThere are {} cards with '{}' in the '{}' category."
"\nThere are no cards with '{}' in the '{}' category."
"\nEnter decklist filename: "
"\nThanks for your support in Yu-Gi-Oh! TCG"

MENU = "\nYu-Gi-Oh! Card Data Analysis" \
           "\n1) Check All Cards" \
           "\n2) Search Cards" \
           "\n3) View Decklist" \
           "\n4) Exit" \
           "\nEnter option: "

CATEGORIES = ["id", "name", "type", "desc", "race", "archetype", "card price"]

def open_file(prompt_str):
    while True:
        filename = input(prompt_str)
        try: # tries to open the file
            fp = open(filename, "r", encoding="utf-8")
            break
            
        except FileNotFoundError:
            print("\nFile not Found. Please try again!")
    return fp
        

def read_card_data(fp):
    
    
    fp.readline()
    # skips the header
    contents = csv.reader(fp) #reads the file and extracts the content to "contents"
    
        
   
    
    card_data = [] #initialize the list for the card data
    for card in contents: #going over every card in the contents 
        id = (card[0])
        name = card[1]
        name = name[:45]
        type = card[2]
        description = card[3]
        race = card[4]
        archetype = card[5]
        tcgprice = float(card[6]) # converts to float for later calculations
        card_data.append((id, name, type, description, race, archetype, tcgprice))  #appending the data to the list
    card_data.sort(key=itemgetter(6, 1)) #sort by price first, then by name in ascending order 
    return card_data


def read_decklist(fp, card_data):
    contents = fp.readlines()
    ids = []
    for card_id in contents:
        ids.append(card_id.strip()) # turns the string into list of strings
        
    deck_list = []
    for card in card_data:  
        for id in ids: # check for each id in the decklist for each card in the card_data
            if card[0] == id:   
                deck_list.append(card)
        deck_list.sort(key=itemgetter(6, 1)) #sort by price first, then by name in ascending order 
    return deck_list

        
def search_cards(card_data, query, category_index):
    result = [] # initialize the result list
    
    for card in card_data:
        if str(query) in str([card[category_index]]): # convert the category and query to string to compare
            result.append(card)
        result.sort(key=itemgetter(6, 1)) #sort by price first, then by name in ascending order 
    return result

def compute_stats(card_data):
    prices = [] # initialize prices list
    for card in card_data:
        prices.append(card[6]) # append price of each card
    min_price = min(prices)
    max_price = max(prices)
    if len(prices) % 2 == 0: # if the length of the list is even
        median_price_1 = sorted(prices)[len(prices) // 2] 
        median_price_2 = sorted(prices)[len(prices) // 2 - 1] / 2 # for two similar middle numbers
        if median_price_1 > median_price_2: #algorithm for finding the median of the list
            median_price = median_price_1
        else:
            median_price = median_price_2
    elif len(prices) % 2 != 0: # if the length of the list is odd
        median_price = sorted(prices)[len(prices) // 2]
    
    min_cards = [] #initialize the lists for the cards 
    max_cards = []
    median_cards = []

    for card in card_data: #appending cards to the list based on the price
        if card[6] == min_price:
            min_cards.append(card)
        if card[6] == max_price:
            max_cards.append(card)
        if card[6] == median_price:
            median_cards.append(card)

    return (min_cards, min_price, max_cards, max_price, median_cards, median_price)


def display_data(card_data):
    print(f'{"Name":50}{"Type":30}{"Race":20}{"Archetype":40}{"TCGPlayer":12}')
    total_price = 0 
    for card in card_data:
        print(f'{card[1]:50}{card[2]:30}{card[4]:20}{card[5]:40}{card[6]:12,.2f}') #rounding the price to 2 decimal places
        total_price += card[6]                                                     # comma for thousands separator
    print(f'\n{"Totals":50}{"":30}{"":20}{"":40}{total_price:12,.2f}')

def display_stats(min_cards, min_price, max_cards, max_price, median_cards, median_price):
    print(f"\nThe price of the least expensive card(s) is {min_price:,.2f}") 
    for card in min_cards:
        print(f"\t{card[1]}")
    print(f"\nThe price of the most expensive card(s) is {max_price:,.2f}")
    for card in max_cards:
        print(f"\t{card[1]}")
    print(f"\nThe price of the median card(s) is {median_price:,.2f}")
    for card in median_cards:
        print(f"\t{card[1]}")
        
def main():
    fp = open_file(prompt_str) #prompt for the file name
    card_data = read_card_data(fp) #parsing the file
    
    while True:
        option = input(MENU)
        if option == "1":
            cheapest_50 = card_data[:50] #slicing the first 50 cards as the list is in ascending oder
            print("There are {} cards in the dataset.".format(len(card_data)))
            display_data(cheapest_50)
            min_cards, min_price, max_cards, max_price, median_cards, median_price = compute_stats(card_data)
            display_stats(min_cards, min_price, max_cards, max_price, median_cards, median_price)
            continue
            
        if option == "2":
            query = input("\nEnter query: ")
            category = input("\nEnter category to search: ").lower()
            
            while category not in CATEGORIES: # checks for valid category input
                print("\nIncorrect category was selected!")
                category = input("\nEnter category to search: ").lower()
            
            category_index = CATEGORIES.index(category) # get the index of the category
            result = search_cards(card_data, query, category_index)
            print("\nSearch results")
            if len(result) != 0: # if the result is not empty
                
                print("\nThere are {} cards with '{}' in the '{}' category.".format(len(result), query, category))
                display_data(result)
                min_cards, min_price, max_cards, max_price, median_cards, median_price = compute_stats(result)
                display_stats(min_cards, min_price, max_cards, max_price, median_cards, median_price)
            else: #otherwise
                print("\nThere are no cards with '{}' in the '{}' category.".format(query, category))
            
            continue
        if option == "3":
            decklist_filename = input("\nEnter decklist filename: ")
            print("\nSearch results")
            try:
                with open(decklist_filename, "r", encoding="utf-8") as deck_fp: #open the decklist file    
                    deck_list = read_decklist(deck_fp, card_data)
                    display_data(deck_list)
                    min_cards, min_price, max_cards, max_price, median_cards, median_price = compute_stats(deck_list)
                    display_stats(min_cards, min_price, max_cards, max_price, median_cards, median_price)
            except FileNotFoundError: # in case wrong or invalid input
                print("\nFile not Found. Please try again!")
            continue

        elif option == "4":
            break
        else:
            print("\nInvalid option. Please try again!")
            continue # in case of invalid input prompt the user again
    fp.close()
    print("\nThanks for your support in Yu-Gi-Oh! TCG")
    
    
    


if __name__ == "__main__":
    main()

