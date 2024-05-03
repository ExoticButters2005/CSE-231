"""
COMPUTER PROJECT 04
MAKE_POPULATION FUNCTION:
        creates population string
        loops amount of times as numpopulation
        creates population based on random sentences same length as target and amount of times
        as numpopulation
        returns population
FITNESS FUNCTION:
        sets fitness score to zero, lowest possible score
        goes through index of characters number of times based on len of target
        final score is fitness score divided by len of target
        returns final score
FIVE_TOURNAMENT_SELECTION FUNCTION:
        best_fitness equals -1 in case of fitness score equals zero
        initializes best_individual
        ets 5 random indivduals using random index 
        sorts out the highest scoring individual and returns it
SINGLE_POINT_CROSSOVER FUNCTION:
        gets random crossover chance to be compared with probability 
        if crossover chance smaller or equal to probability:
            returns new individuals with crossover point 
        else:
            returns original individuals
MUTATION FUNCTION:
        goes through index of characters number of times based on len of individual
        if random chance is smaller than probability:
            returns new individual with random character
        else:
            returns original individual
FIND_BEST_INDIVIDUAL FUNCTION:
        initializes best_individual
        best_fitness equals -1 in case of fitness score equals zero
        goes through index of characters number of times based on len of target
        returns best individual
MAIN FUNCTION:
        prints banner
        while true:  #outer loop to ask user after every run
            checks input
            if anything else but y instantly breaks
            while true:
                gets target input
                checks if input was valid
                initializes new population
                initializes best individual of each gen
                loops numbers of generations
                 loops number of populations
                   sorts through best individuals of each gen
                   adds them to new_population
                
                    update new_population
                    finds best individual of new_population
                    prints number of generations till it reaches target or limit
                    if matches target
                     returns best individual and break loop
                    if reached limit (num_generation)
                     also returns best individual and break loop
                    
                    
                    
"""
import random
#DO NOT CHANGE THIS
random.seed(10)

NUM_GENERATIONS = 200
NUM_POPULATION = 100
PROBABILITY_MUTATION = 0.2
PROBABILITY_CROSSOVER = 0.8
ALPHABET = 'abcdefghijklmnopqrstuvwxyz '

BANNER = """
**************************************************************
Welcome to GeneticGuess Sentencer!
This program will attempt to guess a sentence that you input.
Simply input a sentence and the program will attempt to guess it!
**************************************************************
"""



"\nPlease input the sentence you would like the program to guess: "
"\nIncorrect input. Please try again.\n"
"\n\nGeneticGuess results:"
"Generation: "
"I found the sentence early!"
"\nBest Individual: "
"\n\nThank you for using GeneticGuess Sentencer!"

def make_population(target):
    population = ""
    i = 0
    for i in range(NUM_POPULATION): #loops through the number of population
        for n in range(len(target)):
            individual = random.choice(ALPHABET) #creates individuals each time through the loop
            population += individual #adds individual to population

    return population
def fitness(target, individual):
    fitness_score = 0 #lowest possible score
    i = 0
    for i in range(len(target)): #loops through index of characters number of times based on len of target
        if individual[i] == target[i]: #comparison
            fitness_score += 1 # adds up if true
    final = fitness_score/len(target) # final score
    return final
def five_tournament_selection(population, target):
    tournament_size = 5
    i = 0
    best_fitness = -1 #accounts for score = 0
    best_individual = None
    for i in range(tournament_size):
        starting_index = random.randint(0, NUM_POPULATION-1) *len(target) #beginning index
        ending_index = starting_index + len(target) #ending index
        individual = population[starting_index:ending_index] #takes random individual
        fitness_score = fitness(target, individual) # sorts out best individual based on fitness score
        if fitness_score > best_fitness:
            best_fitness = fitness_score
            best_individual = individual
    return best_individual

def mutation(individual):
    i = 0
    for i in range(len(individual)):
        if random.random() <= PROBABILITY_MUTATION:
            individual = individual[:i] + random.choice(ALPHABET) + individual[i+1:]
    return individual
# mutation_string = mutation(best_result)
def single_point_crossover(individual1, individual2):
    if random.random() <= PROBABILITY_CROSSOVER: # chance of crossover by random
        crossover_point = random.randint(1, len(individual1))
        i1 = (individual1[:crossover_point] + individual2[crossover_point:])
        i2 = (individual2[:crossover_point] + individual1[crossover_point:])
        return i1, i2 # if happened i1 and i2 would be the new individuals value
    else:
        return individual1, individual2 #else

def find_best_individual(population, target):
    best_individual = None
    best_fitness = -1 #accounts for 0 score once again
    for i in range(NUM_POPULATION):
        for n in range(len(target)):
            individual = population[i*len(target): (i+1)* len(target)] #slicing up the population to iterate through every individual
            fitness_score = fitness(target, individual) #sorting out
            if fitness_score > best_fitness: #algorithm for finding most fit individual
                best_fitness = fitness_score
                best_individual = individual
    return best_individual

def main():
    print(BANNER)
    while True: #INPUT loop
        INPUT = input("\nWould you like to continue? (y/n) ").lower()
        if INPUT != 'y':
            print("\nThank you for using GeneticGuess Sentencer!")
            break
        # This input prompt is in the outer loop, so it is repeated after each run

        while True: #main loop
            target = input("Please input the sentence you would like the program to guess: ").lower()
            if all(char in ALPHABET for char in target):
                population = make_population(target) #creates population
                print("\n\nGeneticGuess results:")
                for generation in range(NUM_GENERATIONS): #loops through the number of generations
                    new_population = ""
                    true_individual = "" #initializes new population and best individual of every generation
                    for i in range(NUM_POPULATION): #loops through the number of population
                        individual1 = five_tournament_selection(population, target)
                        individual2 = five_tournament_selection(population, target)
                        individual1 = mutation(individual1)
                        individual2 = mutation(individual2)
                        individual1, individual2 = single_point_crossover(individual1, individual2)
                        fitness_score1 = fitness(target, individual1)
                        fitness_score2 = fitness(target, individual2)
                        if fitness_score1 > fitness_score2: #algorithm for finding best individual between the 2
                            best_individual1 = individual1
                        else:
                            best_individual1 = individual2
                        if best_individual1 == target:
                            true_individual = best_individual1  # saves the best individuals of each generation
                        new_population += str(best_individual1) # adds up all the best individuals of each generation
                    population = new_population
                    best_individual = find_best_individual(population, target)
                    print("Generation: ", generation)
                    if true_individual == target: #break if found most fit individual
                        print("I found the sentence early!")
                        print("\nBest Individual: ", best_individual)
                        break
                    elif generation == NUM_GENERATIONS-1: #reached the generation limit at 199
                        print("Best Individual: ", best_individual)
                        break
                break  # Break from the inner loop
            else:
                print("\nIncorrect input. Please try again.\n")
                
                
if __name__ == '__main__':
    main()
# skeleton code at the bottom