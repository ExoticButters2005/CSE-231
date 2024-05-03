""" write your English pseudocode here (No code) 
A pseudocode can later be easily translated into a program. 
Pseudocode can become your code header, docstrings, and comments in your program.
# Pseudocode for Project 6
main():
    # Get file names from user
    names_file = prompt user for names file
    twitter_file = prompt user for Twitter file
    facebook_file = prompt user for Facebook file

    # Read files and construct nested dictionary
    social_network = read_files(names_file, twitter_file, facebook_file)

    # Main menu loop
    While True:
        print menu
        user input = input() 
        If input is 1:
            Call function
            print max intersection of friends
            continue
        Elif input is 2:
            Call function
            print percentage with no shared friends
            continue
        Elif input is 3:
            Call function
            print individual information
            continue
        Elif input is 4:
            Call function
            print percentage with more friends in X
            continue
        Elif input is 5:
            Call function
            print triangle friendships in X
            continue
        Elif input is 6:
            Call function
            print triangle friendships in Facebook
            continue
        Elif input is 7:
            Call function
            print triangle friendships in X and Facebook
            continue
        Else:
            Print "Thank you"
            break

# Function to read files and return nested dictionary
Function read_files(names_file, twitter_file, facebook_file):
    initializes 3 lists for each files
    read first file and append results to first list
    read second file and append results to second list
    read third file and append results to third list
  
    Return nested dictionary

# Function to print menu
Function print_menu:
    # Print menu options


max_intersection(social_network):
    max_intersection_size = 0
        
        for person in X:
            person_friends = person from set X
            facebook_friends = person from set Facebook
            intersection_size = len(person_friends.intersection(facebook_friends))
            
            if intersection_size > max_intersection_size:
                max_intersection_size = intersection_size
        
        return max_intersection_size
percentage_no_shared_friends(social_network):
    count_more_friends_in_x = 0
    total_individuals = len(social_network)

    for person, networks in social_network.items():
        if friends_in_x > friends_in_facebook:
            count_more_friends_in_x += 1

    percentage = round((count_more_friends_in_x / total_individuals) * 100)
    return percentage

individual_information(social_network):
    # Prompt for name and print friends in X and Facebook

percentage_more_friends_in_x(social_network):
    # Calculate and print percentage

_triangle_friendships_in_x(social_network):
    # Calculate and print number of triangle friendships

triangle_friendships_in_facebook(social_network):
    # Calculate and print number of triangle friendships

triangle_friendships_in_x_and_facebook(social_network):
    # Calculate and print number of triangle friendships
    Call main function
skeleton code in the end
 runs main function

"""
# S = {900, 400, 700, 800}
# S.discard( 900 )

# print( S )
# S = { 10, 20, 30, 40 }
# T = { 30, 40, 50 }
# U = { 10, 30 }

# # print( S | T )
# S = { 10, 20, 30, 40 }
# T = { 30, 40, 50 }
# U = { 10, 30 }

# print( S & T )
S = { 10, 20, 30, 40 }
T = { 30, 40, 50 }
U = { 10, 30 }

# print( S ^ T)
S.issuperset( S )


