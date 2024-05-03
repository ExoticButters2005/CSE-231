""" 
open_file func(fp, choice = ""):
 takes in fp
 while True
 attempts to open fp using try except
 else file not found, print error message according to each respective missing file and continue
csv_reader func(fp):
  creates an empty list
  takes in fp
  csv.reader(fp)
  adds each line to a list
file_reader func(fp):
  takes in fp
  creates empty list
  for each line in the file
  if not empty, append, else append empty list
twitter_decoder func():
  creates empty list
  matches the id to the index position in the names list
  append the matches
  return the list
dict_nester func(facebook_friends and twitter friends):
  creates a dictionary of using names and friends
  keys = names from names list
  friends = either facebook or twitter friends
count_triangles func():
  finds people who share friends
  if the friend of a friend is in the friends list and not the same as the person
  add the triangle to the set
  return the number of triangle friendships
max_common_friends func():
  finds the maximum number of common friends between X and FB
  finds the intersection of the values of the key in X and FB
  returns the max common friends
percentage_no_shared_friends func():
  finds people with no shared friends
  find by comparing if they are in the intersection of the values of the key in X and FB
  returns the percentage of people with no shared friends as an integer  
individual_information func():
  prints the friends of a person in twitter and facebook
percentage_more_friends_in_X func():
  finds len of friends of people in x
  if len values in X is greater than len values in FB
  add to the count
  percentage = total number of people in X with more friends/ total number of people in X
  converts final result to integer
triangle_friendships_in_X_and_FB func():
  merges friends in X and FB
  returns the number of triangle friendships in the merged friends
main func():
  opens each files
  reads each file
  decodes the twitter friends
  while True:
   print menu
   ask for choice
   continue to ask after each choice
   break loop when any other input is entered
"""
import csv 
import sys

def input( prompt=None ):
    """
        DO NOT MODIFY: Uncomment this function when submitting to Codio
        or when using the run_file.py to test your code.
        This function is needed for testing in Codio to echo the input to the output
        Function to get user input from the standard input (stdin) with an optional prompt.
        Args:
            prompt (str, optional): A prompt to display before waiting for input. Defaults to None.
        Returns:
            str: The user input received from stdin.
    """

    if prompt:
        print( prompt, end="" )
    aaa_str = sys.stdin.readline()
    aaa_str = aaa_str.rstrip( "\n" )
    print( aaa_str )
    return aaa_str


choices = '''
  Menu : 
     1: Max number of friends intersection between X and Facebook among all
     2: Percentage of people with no shared friends between X and Facebook
     3: Individual information
     4: Percentage of people with  more friends in X compared to Facebook
     5: The number of  triangle friendships in X
     6: The number of  triangle friendships on Facebook
     7: The number of  triangle friendships in X and Facebook together 
       Enter any other key(s) to exit

  '''

"Input a choice ~:"

"Error. File does not exist"
"\nEnter a names file ~:"
"\nEnter the X id file ~:"
"\nEnter the facebook id file ~:"

"The Max number intersection of friends between X and Facebook is: {}"
"{}% of people have no friends in common on X and Facebook"

# "Enter a person's name ~:"
# print("-"*14+"\nFriends in X\n"+"*"*14)
# print("-"*20+"\nFriends in Facebook\n"+"*"*20)
"Invalid name or does not exist"

"{}% of people have more friends in X compared to Facebook"

"The number of triangle friendships in X is: {}"
"The number of triangle friendships in Facebook is: {}"
"The number of triangle friendships in X merged with Facebook is:  {}"
"Thank you"


def open_file(fp, choice = ""):
  while True:
    try:
      file = open(fp)
      return file
    except FileNotFoundError:
      print("Error. File does not exist")
      if choice == "X":
        fp = input("\nEnter the twitter id file ~:")
      elif choice == "FB":
        fp = input("\nEnter the facebook id file ~:")
      else:
        fp = input("\nEnter a names file ~:")
      
def csv_reader(fp):
  names_lst = []
  contents = csv.reader(fp)
  for names in contents: # for each line within the string returned by csv.reader
    names_lst.append(names) # append the names to the names_lst
  return names_lst
def file_reader(fp):
  friends = [] # initializes empty list to store friends
  
  for lines in fp:
    if lines == "\n": # if the line is empty append an empty list
      friends.append([])
      
    else: # if the line is not empty
      lines = lines.strip(", \n").split(",")
      friends.append(lines) # append the line to the friends list
  return friends
def twitter_decoder(friends, names_lst):
    twitter_friends = [] # initializes empty list for twitter/X friends
    for lines in friends:
        person_friends = [] # initializes empty list for each person's friends
        for friend in lines: # for each element in list(lines)
            if friend: # if the element is not empty
                friend = int(friend) # convert to integer
                person_friends.append(names_lst[friend][0]) # append the name of the friend to the person's friends list
        twitter_friends.append(person_friends) # append the person's friends list to the twitter/X friends list
    return twitter_friends
def dict_nester(names_lst, friends):
    friends_dct = {} # initializes empty dictionary
    for key, friend_list in zip(names_lst, friends): # for each name and friend list in the names list and friends list
        dict_key = key[0]  # first element in the name list is the key
        friends_dct[dict_key] = friend_list
    return friends_dct

def count_triangles(friends_dict):
    triangles = set() # initializes empty set 
    for person, friends in friends_dict.items():
        for friend in friends: # for each value in values of friends_dict
            for friend_of_friend in friends_dict.get(friend, []): 
                if friend_of_friend in friends and friend_of_friend != person: # if the friend of friend is in the friends list and not the same as the person
                    triangle = tuple(sorted((person, friend, friend_of_friend))) # new triangle tuple 
                    triangles.add(triangle) # add the triangle to the set
    
    return len(triangles) # return the number of triangle friendships
# OPTION 1
def max_common_friends(people_in_X, people_in_FB):
    max_common = 0
    for person, friends_in_X in people_in_X.items():
        if person in people_in_FB: # if key in X is in FB
            common_friends = set(friends_in_X).intersection(people_in_FB[person]) # find the intersection of the values of the key in X and FB
            if len(common_friends) > max_common:
                max_common = len(common_friends) #algorithm for finding max common friends
                # person_with_max_common = person
    return max_common
# OPTION 2
def percentage_no_shared_friends(people_in_X, people_in_FB):
    total_people = len(people_in_X) # total number of people in X
    no_shared = sum(1 for person, friends_in_X in people_in_X.items() # sum of people with no shared friends
                    if not set(friends_in_X).intersection(set(people_in_FB.get(person, [])))) # if the intersection of the values of the key in X and FB is empty
    return int((no_shared / total_people) * 100) #converts to integer
# OPTION 3
def individual_information(people_in_X, people_in_FB):
    name = input("Enter a person's name ~: ")
    print("-" * 14)

    # Friends in X
    print("Friends in X")
    print("*" * 14)
    if name in people_in_X:
        for friend in sorted(people_in_X[name]):
            print(friend)
    print("-" * 20)

    # Friends in Facebook
    print("Friends in Facebook")
    print("*" * 20)
    if name in people_in_FB:
        for friend in sorted(people_in_FB[name]):
            print(friend)
    print("-" * 20)
# OPTION 4
def percentage_more_friends_in_X(people_in_X, people_in_FB):
    more_in_X = sum(1 for person, friends_in_X in people_in_X.items() # sum of people with more friends in X compared to FB
                    if len(friends_in_X) > len(people_in_FB.get(person, []))) # if len values in X is greater than len values in FB
    return int((more_in_X / len(people_in_X)) * 100) # also converts to integer
# OPTION 5
def triangle_friendships_in_X(people_in_X):
    return count_triangles(people_in_X) # returns the number of triangle friendships in X
# OPTION 6
def triangle_friendships_in_FB(people_in_FB):
    return count_triangles(people_in_FB) # returns the number of triangle friendships in FB
# OPTION 7
def triangle_friendships_in_X_and_FB(people_in_X, people_in_FB):
    merged_friends = {}
    for person in people_in_X: # for each key in X
        merged_friends[person] = set(people_in_X[person]).union(people_in_FB.get(person, [])) # merge the values of the key in X and FB
    
    for person in people_in_FB:
        if person not in merged_friends:
            merged_friends[person] = set(people_in_FB[person]) # if the key in FB is not in the merged friends, add the values of the key in FB
    
    return count_triangles(merged_friends) # returns the number of triangle friendships in the merged friends


        
        
    
def main():
  file_names_path = input("\nEnter a names file ~:") # input for the names file
  file_names = open_file(file_names_path) # opens the names file
  names = csv_reader(file_names) # reads the names file
  file_X_path = input("\nEnter the twitter id file ~:")
  file_X = open_file(file_X_path, "X")
  X = file_reader(file_X)
  file_FB_path = input("\nEnter the facebook id file ~:")
  file_FB = open_file(file_FB_path, "FB")
  fb = file_reader(file_FB)
  twitter_friends = twitter_decoder(X, names)
  people_in_X = dict_nester(names, twitter_friends) # dictionary of people in X
  
  people_in_FB = dict_nester(names, fb) # dictionary of people in FB
  while True:
    print(choices) # choices menu
    option = input("Input a choice ~:") # input for the choice
    if option == "1":
      result = max_common_friends(people_in_X, people_in_FB)
      print(f"The Max number intersection of friends between X and Facebook is: {result}")
      continue
    elif option == "2":
      result = percentage_no_shared_friends(people_in_X, people_in_FB)
      print(f"{result}% of people have no friends in common on X and Facebook")
      continue
    elif option == "3":
      individual_information(people_in_X, people_in_FB)
      continue
    elif option == "4":
      result = percentage_more_friends_in_X(people_in_X, people_in_FB)
      print(f"{result}% of people have more friends in X compared to Facebook") 
      continue
    elif option == "5":
      result = triangle_friendships_in_X(people_in_X)
      print(f"The number of triangle friendships in X is: {result}")
      continue
    elif option == "6":
      result = triangle_friendships_in_FB(people_in_FB)
      print(f"The number of triangle friendships in Facebook is: {result}")
      continue
    elif option == "7":
      result = triangle_friendships_in_X_and_FB(people_in_X, people_in_FB)
      print(f"The number of triangle friendships in X merged with Facebook is:{result}")
      continue # continues the loop
    else: # in case of any other input
      print("Thank you")
      break
  file_names.close() # closes the file and hopefully saves memory 
  
  


if __name__ == '__main__':
  main()

