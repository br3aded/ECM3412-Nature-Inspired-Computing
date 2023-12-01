from ant_colony import get_distance_matrix,inital_pheromone,get_heuristic_matrix,ant_path,calculate_transition_probabilities,distance_cost

#this function enforces our min and max values of the pheromones
def enforce_pheromone_limits(pheromone_matrix,pheromone_max,pheromone_min):
    for i in range(len(pheromone_matrix)):
        for j in range(len(pheromone_matrix)):
            #limit pheromone with min and max functions
            pheromone_matrix[i][j] = max(pheromone_min,min(pheromone_max,pheromone_matrix[i][j]))

#this functions updates the pheromones using the rules from min max ant colony
def pheromone_update_mmas(ant_paths,pheromone_matrix,distance_matrix,q,pheromone_max,pheromone_min,evaporate_rate):
    #find the best path from the iteration
    best_path = min(ant_paths,key=lambda path:distance_cost(path,distance_matrix))

    #for each of the paths evaporate and add pheromones if its the best path in the iteration
    for path in ant_paths:
        for i in range(len(path)-1):
            delta_tau = q/distance_cost(path,distance_matrix) if path == best_path else 0
            pheromone_matrix[path[i]][path[i+1]] = (1 - evaporate_rate) * pheromone_matrix[path[i]][path[i+1]] + delta_tau
    #call function to enforce pheromone limits
    enforce_pheromone_limits(pheromone_matrix,pheromone_max,pheromone_min)

#main function used to call ant colony mmas
def ant_colony_optimisation_mmas(xml_file,ant_num,evaporate_rate,q_value,fitness_evaluations,pheromone_max,pheromone_min):
    #call functions to get the distance matrix , heurstic matrix and phermone matrix
    distance_matrix = get_distance_matrix(xml_file)
    heuristic_matrix = get_heuristic_matrix(distance_matrix, q_value)
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

        #update pheromones
        pheromone_update_mmas(ant_paths,pheromone_matrix,distance_matrix,q_value,pheromone_max,pheromone_min,evaporate_rate)
    print(best_solution)