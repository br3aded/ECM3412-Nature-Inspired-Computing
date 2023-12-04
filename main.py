from ant_colony import ant_colony_optimisation
from elitism_ant_colony import elitism_ant_colony_optimisation
from min_max_ant_colony import ant_colony_optimisation_mmas
import time

#function used for testing the affect number of ants has on our results
def ant_number_tests():
    #set variables
    data_sets = ["burma.xml" , "brazil.xml"]
    ant_numbers = [10,25,50,75,100]
    test_num = 0

    #open file to write data 
    file_path = 'ant number test data.txt'
    file = open(file_path, 'w')
    #loops for both burma and brazil data sets
    for data in data_sets:
        file.write(str(data) + " Results:\n")
        if data == 'burma.xml':
            test_num = 10
        else:
            test_num = 5
        #loops through are different variables tests
        for i in range(len(ant_numbers)):
            file.write("Number of Ants : " + str(ant_numbers[i]) + "\n")
            print("Number of Ants : " + str(ant_numbers[i]))
            best_solution = [100000,0,0]
            average_solution = 0
            average_convergence = 0
            #run multiple times to get average results
            for j in range(test_num):
                solution = ant_colony_optimisation(data,ant_numbers[i],0.5,3,10000)
                #find best solution
                if solution[0] < best_solution[0]:
                    best_solution = solution
                #take average results
                average_solution += solution[0]
                average_convergence += solution[2]
                #output result
                file.write("test " + str(j+1) + "| solution : " + str(solution[0]) + " | convergence : " + str(solution[2]) + "\n")
            #calculate overall average
            average_solution = average_solution / test_num
            average_convergence = average_convergence / test_num
            #output final results
            file.write("Overall Results | Best Solution : " +  str(best_solution[0]) + " | Average Solution : " + str(average_solution) + "| Average Covengence :" + str(average_convergence) + "\n")
            file.write('\n')
        file.write('\n')
    file.close()

#function used for testing the affect the evaporation rate has on our results
def evaporation_rate_tests():
    #set variables
    data_sets = ["burma.xml" , "brazil.xml"]
    evaporation_rates = [0.9,0.7,0.5,0.3,0.1]
    test_num = 0

    #open file to write data 
    file_path = 'evaporation rate test data.txt'
    file = open(file_path, 'w')
    #loops for both burma and brazil data sets
    for data in data_sets:
        file.write(str(data) + " Results:\n")
        if data == 'burma.xml':
            test_num = 10
        else:
            test_num = 5
        #loops through are different variables tests
        for i in range(len(evaporation_rates)):
            file.write("Evaporation Rate : " + str(evaporation_rates[i]) + "\n")
            best_solution = [100000,0,0]
            average_solution = 0
            average_convergence = 0
            #run multiple times to get average results
            for j in range(test_num):
                solution = ant_colony_optimisation(data,50,evaporation_rates[i],3,10000)
                #find best solution
                if solution[0] < best_solution[0]:
                    best_solution = solution
                #take average results
                average_solution += solution[0]
                average_convergence += solution[2]
                #output result
                file.write("test " + str(j+1) + "| solution : " + str(solution[0]) + " | convergence : " + str(solution[2]) + "\n")
            #calculate overall average
            average_solution = average_solution / test_num
            average_convergence = average_convergence / test_num
            #output final results
            file.write("Overall Results | Best Solution : " +  str(best_solution[0]) + " | Average Solution : " + str(average_solution) + "| Average Covengence :" + str(average_convergence) + "\n")
            file.write('\n')
        file.write('\n')
    file.close()

#function used for testing the affect the q value has on our results
def q_value_tests():
    #set variables
    data_sets = ["burma.xml" , "brazil.xml"]
    q_value = [1,2,3,4,5]
    test_num = 0

    #open file to write data 
    file_path = 'q value test data.txt'
    #used for heurstic function q/d data 
    #file_path = 'q over d heuristic test data.txt'

    file = open(file_path, 'w')
    #loops for both burma and brazil data sets
    for data in data_sets:
        file.write(str(data) + " Results:\n")
        if data == 'burma.xml':
            test_num = 10
        else:
            test_num = 5
        #loops through are different variables tests
        for i in range(len(q_value)):
            file.write("Q Value : " + str(q_value[i]) + "\n")
            best_solution = [100000,0,0]
            average_solution = 0
            average_convergence = 0
            #run multiple times to get average results
            for j in range(test_num):
                solution = ant_colony_optimisation(data,50,0.5,q_value[i],10000)
                #find best solution
                if solution[0] < best_solution[0]:
                    best_solution = solution
                #take average results
                average_solution += solution[0]
                average_convergence += solution[2]
                #output result
                file.write("test " + str(j+1) + "| solution : " + str(solution[0]) + " | convergence : " + str(solution[2]) + "\n")
            #calculate overall average
            average_solution = average_solution / test_num
            average_convergence = average_convergence / test_num
            #output final results
            file.write("Overall Results | Best Solution : " +  str(best_solution[0]) + " | Average Solution : " + str(average_solution) + "| Average Covengence :" + str(average_convergence) + "\n")
            file.write('\n')
        file.write('\n')
    file.close()

#used to test one ant colony , can be used for different variations of ant colony , outputs to console
def ant_colony_test():
    data_sets = ["burma.xml" , "brazil.xml"]
    test_num = 0

    for data in data_sets:
        print(str(data) + " Results:")
        if data == 'burma.xml':
            test_num = 10
        else:
            test_num = 5
        best_solution = [100000,0,0]
        average_solution = 0
        average_convergence = 0
        for j in range(test_num):
            #solution = elitism_ant_colony_optimisation(data,100,0.1,5,10000)
            solution = ant_colony_optimisation_mmas(data,100,0.1,5,10000,2,0.1)
            #solution = ant_colony_optimisation(data,50,0.5,3,10000)
            if solution[0] < best_solution[0]:
                best_solution = solution
            average_solution += solution[0]
            average_convergence += solution[2]
            print("test " + str(j+1) + "| solution : " + str(solution[0]) + " | convergence : " + str(solution[2]))
        average_solution = average_solution / test_num
        average_convergence = average_convergence / test_num
        print("Overall Results | Best Solution : " +  str(best_solution[0]) + " | Average Solution : " + str(average_solution) + "| Average Covengence :" + str(average_convergence))
        

if __name__ == '__main__':
    #variables that can be changed 
    file_name = "brazil.xml"
    ant_number = 100
    evaporate_rate = 0.3
    q_value = 1
    fitness_evaluations = 10000
    pheromone_max = 2.0
    pheromone_min = 0.1

    #different implementations of ant colony
    #result = ant_colony_optimisation(file_name,ant_number,evaporate_rate,q_value,fitness_evaluations)
    #print(result)
    #elitism_ant_colony_optimisation(file_name,ant_number,evaporate_rate,q_value,fitness_evaluations)
    #ant_colony_optimisation_mmas(file_name,ant_number,evaporate_rate,q_value,fitness_evaluations,pheromone_max,pheromone_min)

    #different test functions
    ant_colony_test()
    #ant_number_tests()
    #evaporation_rate_tests()
    #q_value_tests()
   
   