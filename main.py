from ant_colony import ant_colony_optimisation
from elitism_ant_colony import elitism_ant_colony_optimisation
from min_max_ant_colony import ant_colony_optimisation_mmas
import time

if __name__ == '__main__':
    #variables that can be changed 
    file_name = "brazil.xml"
    ant_number = 100
    evaporate_rate = 0.3
    q_value = 1
    fitness_evaluations = 10000
    pheromone_max = 2.0
    pheromone_min = 0.1

    """
    start_time = time.time()
    ant_colony_optimisation(file_name,ant_number,evaporate_rate,q_value,fitness_evaluations)
    end_time = time.time()
    print(end_time-start_time)
    """
    
    start_time = time.time()
    elitism_ant_colony_optimisation(file_name,ant_number,evaporate_rate,q_value,fitness_evaluations)
    end_time = time.time()
    print(end_time-start_time)
"""
    start_time = time.time()
    ant_colony_optimisation_mmas(file_name,ant_number,evaporate_rate,q_value,fitness_evaluations,pheromone_max,pheromone_min)
    end_time = time.time()
    print(end_time-start_time)
    """
    #run tests for 5 values for each variable
    #ant nums - 10 , 25 , 50 , 75 , 100
    #evaporation - 0.9 , 0.7 ,0.6 , 0.5 , 0.3 
    # q value - 1 , 2 , 3 , 4 , 5
    #run test 10 times to get average , best fitness and average convergence
    #carry this out for both the burma and brazil data sets
    #test change of ant number , evaporation rate and q_value
    #output this to a text file showing each run and the final results for each 

    #run test for out alternative fitness function , testing what happens when we vary q
    #implement 