import xml.etree.ElementTree as ET
import random
import copy
import time
import numpy as np


#function turns the data in xml file into the distance matrix D
def get_distance_matrix(xml_file):
    #get the graph from the file 
    graph = ET.parse(xml_file).getroot().findall('.//vertex')
    
    data = []
    current_vertex = 0
    #loop for citys in the graph
    for vertex in graph:
        #get all the edges for the city
        edges = vertex.findall('.//edge')
        edge_data = []
        current_edge = 0
        #loop through edges in city
        for edge in edges:
            if(current_vertex == current_edge):
                #set citys own cost to 0
                edge_data.append(int(0))
            #add cost to the list
            edge_data.append(float(edge.get('cost')))
            current_edge += 1
        #add city data to distance matrix
        data.append(edge_data)
        current_vertex += 1
    #add 0 to the final entry in the final city in the list
    data[len(vertex.findall('.//edge'))].append(0)
    return data

def inital_pheromone(size):
    #returns a matrix of size number of citys intiliased with random values between 0.1 and 1
    return [[random.uniform(0.1,1) for i in range(size)] for j in range(size)]

def get_heuristic_matrix(distance_matrix):
    #returns a matrix of values 1/d as heurstic function
    return [[(1/distance_matrix[i][j]) if i !=j else 0 for i in range(len(distance_matrix))] for j in range(len(distance_matrix))]

#this function calculates one ant path
def ant_path(heuristic_matrix,pheromone_matrix):
    city_index = 0
    path = [0]

    #creates a copy of the heurstic matrix
    heuristic_matrix_copy = np.copy(heuristic_matrix)
    #heuristic_matrix_copy = copy.deepcopy(heuristic_matrix)
    #loop for the number of citys our path will have
    for i in range((len(heuristic_matrix))-1):
        #remove current city from the heuristic matrix
        for z in range(len(heuristic_matrix_copy)):
                    heuristic_matrix_copy[z][city_index] = 0
        #uses function to get the cumulative probabilites for the cities
        cumulative_probabilties = calculate_transition_probabilities(heuristic_matrix_copy,pheromone_matrix,city_index)
        #generate a random number to be used for picking which city to go to next
        rand = random.uniform(0.1,1)
        #loop through each city probability
        for j in cumulative_probabilties:
            #if probability is >= our random number we add to path and set as current city
            if j >= rand:
                path.append(cumulative_probabilties.index(j))
                city_index = cumulative_probabilties.index(j)
                break
    #add first city to the end of the path
    path.append(0)
    return path

#this function calculates the cumulative transition probabilites for a given city
def calculate_transition_probabilities(heuristic_matrix,pheromone_matrix,city_index):
    num_cities = len(heuristic_matrix)
    #values used in the formula for calculating the transition probability
    alpha = 1
    beta = 2
    cumulative_probabilties = []

    #calculate the denominator for our tranisiton function formula
    denominator = sum(((pheromone_matrix[city_index][l] ** alpha) * (heuristic_matrix[city_index][l] ** beta)) for l in range(num_cities) if l != city_index)

    #the function calculates the transition probabilites and cumulative transition probabilties at the same time
    for i in range(num_cities):
        #condition for the first city
        if i == 0:
            #checks to see if city index is the current city being looped through
            if city_index == i:
                #sets probabilty to 0 if it is
                cumulative_probabilties.append(0)
            else:
                #if not calculate the numerator using the transition probability formula
                numerator = (pheromone_matrix[city_index][i] ** alpha) * (heuristic_matrix[city_index][i] ** beta)
                #add probability for that city to list
                cumulative_probabilties.append(numerator/denominator)
        #conditions if not first city
        else:
            #checks to see if city index is the current city being looped through
            if city_index == i:
                #addes previous probability as the current probability would be 0
                cumulative_probabilties.append(cumulative_probabilties[i-1])
            else:
                #if not calculate the numerator using the transition probability formula
                numerator = (pheromone_matrix[city_index][i] ** alpha) * (heuristic_matrix[city_index][i] ** beta)
                #adds the previous citys probability and current city probability to get the cumulative probability
                cumulative_probabilties.append(cumulative_probabilties[i-1] + numerator/denominator)
            
    return cumulative_probabilties

def distance_cost(path,distance_matrix):
    cost = 0
    for j in range(len(path)-1):
        cost += distance_matrix[path[j]][path[j+1]]
    cost += distance_matrix[path[-1]][path[1]]
    return cost

def pheromone_update(ant_paths,pheromone_matrix,distance_matrix,q):
    for path in ant_paths:
        cost = distance_cost(path,distance_matrix)
        for i in range(len(path)-1):
            pheromone_matrix[path[i]][path[i+1]] += q/cost

def evaporate_pheromones(pheromone_matrix,evaporate_rate):
    for i in range(len(pheromone_matrix)):
        for j in range(len(pheromone_matrix)):
            pheromone_matrix[i][j] *= (1-evaporate_rate)

def ant_colony(xml_file,ant_num,evaporate_rate,q_value,iteration_number):
    #call functions to get the distance matrix , heurstic matrix and phermone matrix
    distance_matrix = get_distance_matrix(xml_file)
    heuristic_matrix = get_heuristic_matrix(distance_matrix)
    pheromone_matrix = inital_pheromone(len(distance_matrix))
    
    best_solution = [100000,0,0]

    for i in range(iteration_number):
        ant_paths = []
        #initalise and get paths for each ant
        for j in range(ant_num):
            path = ant_path(heuristic_matrix,pheromone_matrix)
            if(distance_cost(path,distance_matrix)<best_solution[0]):
                best_solution[0] = distance_cost(path,distance_matrix)
                best_solution[1] = path
                best_solution[2] = i
            ant_paths.append(path)
        
        #update pheromones
        pheromone_update(ant_paths,pheromone_matrix,distance_matrix,q_value)

        #evaporate pheromones
        evaporate_pheromones(pheromone_matrix,evaporate_rate)

    print(best_solution)
 

if __name__ == '__main__':
    file_name = "burma.xml"
    ant_number = 10
    evaporate_rate = 0.3
    q_value = 1
    iteration_number = 1000

    start_time = time.time()
    ant_colony(file_name,ant_number,evaporate_rate,q_value,iteration_number)
    end_time = time.time()
    print(end_time-start_time)
    
    