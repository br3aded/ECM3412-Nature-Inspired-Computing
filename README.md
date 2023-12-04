# ECM3412-Nature Inspired Computing
 Ant Colony Optimisation Travelling Salesman problem

The program consists of 4 python files main.py , ant_colony.py , elitism_ant_colony.py and min_max_ant_colony.py.
The code is executed from the main file while the other 3 file contains functionality for the implementation of the different variations of ant colony. See file comments for more information on how they work.

Within the main file you can run 1 ant colony run using ant_colony_optimisation(file_name,ant_number,evaporate_rate,q_value,fitness_evaluations)
with the variables:
file_name - name of xml file 
ant_number - number of ants in each iteration
evaporate_rate - rate at which we evaporate the pheromones when updating them
q_value - value used in the formula Q/fitness when updating pheromones
fitnes_evaluations - how many ant will be evaluated before the program terminantes.
The ant_colony_optimisation returns an array with 3 elements those being : cost of best path , the best path , what evaluation number this path was found on.

For different variations of the ant colony run the functions:
elitism_ant_colony_optimisation(file_name,ant_number,evaporate_rate,q_value,fitness_evaluations) - which adds the best solution currenlty found to the paths that get pheromones added
ant_colony_optimisation_mmas(file_name,ant_number,evaporate_rate,q_value,fitness_evaluations,pheromone_max,pheromone_min) - this uses a min max apporach to our pheromone values which can be adjusted using the pheromone_max and pheromone_min variables.

For different variations of heurstic functions these can be changed in ant_colony.py as all the variations use the same function, to change heurstic function see different functions commented out within the get_heuristic_matrix() function and uncomment the one you wish to use. The variations are:
return [[(1/distance_matrix[i][j]) if i !=j else 0 for i in range(len(distance_matrix))] for j in range(len(distance_matrix))] - uses heuristic function 1/d
return [[(q/distance_matrix[i][j]) if i !=j else 0 for i in range(len(distance_matrix))] for j in range(len(distance_matrix))] - uses heuristic function q/d
#return [[(1/distance_matrix[i][j]**2) if i !=j else 0 for i in range(len(distance_matrix))] for j in range(len(distance_matrix))] - uses heuristic function 1/d^n where n here is 2

Inside the main.py file we also have 3 functions for running test:
ant_number_tests() - outputs to text file "ant number test data.txt" results of testing different number of ants with multiple iterations
evaporation_rate_tests() - outputs to text file "evaporation rate test data.txt" results of testing different evaporation rate with multiple iterations
q_value_tests() - outputs to text file "q value test data.txt" results of testing different q values with multiple iterations
the run time for each test is about 18 minutes

The other text files included with the program were made by taking results printed to console and putting them in the text file. These are:
1 over d heursitic test data.txt
1 over d power n herusitic test data.txt
Best Parameters Test Data.txt
elitism ant colony test data.txt
min max ant colony test data.txt
q over d heuristic test data.txt
Q value 10 test data.txt
The names describe what data they contain.