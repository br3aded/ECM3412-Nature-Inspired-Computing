from ant_colony import get_distance_matrix,inital_pheromone,get_heuristic_matrix,ant_path,calculate_transition_probabilities,distance_cost,pheromone_update

def elitism_ant_colony_optimisation(xml_file,ant_num,evaporate_rate,q_value,fitness_evaluations):
    #call functions to get the distance matrix , heurstic matrix and phermone matrix
    distance_matrix = get_distance_matrix(xml_file)
    heuristic_matrix = get_heuristic_matrix(distance_matrix,q_value)
    pheromone_matrix = inital_pheromone(len(distance_matrix))
    
    total_evaluations = 0

    best_solution = [100000,0,0]

    while total_evaluations <= fitness_evaluations:
        ant_paths = []
        #initalise and get paths for each ant
        for j in range(ant_num):
            path = ant_path(heuristic_matrix,pheromone_matrix)
            if(distance_cost(path,distance_matrix)<best_solution[0]):
                best_solution[0] = distance_cost(path,distance_matrix)
                best_solution[1] = path
                best_solution[2] = total_evaluations
            total_evaluations += 1
            ant_paths.append(path)
        
        #add current best solution to the paths to add pheromones to that path
        ant_paths.append(best_solution[1])
        #update pheromones
        pheromone_update(ant_paths,pheromone_matrix,distance_matrix,q_value,evaporate_rate)

    return best_solution