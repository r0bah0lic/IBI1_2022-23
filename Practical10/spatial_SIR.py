import numpy as np 
import matplotlib.pyplot as plt 
population = np. zeros ( (100 , 100) )
outbreak = np. random . choice (range(100) ,2) 
population [ outbreak [0] , outbreak [ 1 ] ] = 1 
beta = 0.3
gamma = 0.05
def update(population, beta, gamma):  #define the infection function
    new_population = population.copy()  #update the population figure
    infected_positions = np.transpose(np.nonzero(population == 1))  #find the positions of infected(population=1)
    for i, j in infected_positions:
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:  #find neighbours
            ni, nj = i + di, j + dj
            if 0 <= ni < 100 and 0 <= nj < 100 and population[ni, nj] == 0:  #if neighbour is S and in 100*100 figure
                if np.random.rand() < beta:  #satisfy the infection probability
                    new_population[ni, nj] = 1  #infect the neighbour
    infected_indices = np.transpose(np.nonzero(new_population == 1))  #update infected positions after infection
    for i, j in infected_indices:
        if np.random.rand() < gamma:  #satisfy the recovery probability
            new_population[i, j] = 2  #revover the infected, recovered=2
    return new_population
for i in range(1,101):
    population = update(population, beta, gamma)
plt.figure(figsize =(6, 4), dpi=150) 
plt.imshow(population, cmap = 'viridis', interpolation = 'nearest')
plt.show()
