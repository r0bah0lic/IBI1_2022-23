import numpy as np 
import matplotlib.pyplot as plt 
N = 10000      #total population
I = 1          #infected person
S = N - I      #susceptive person
R = 0          #recovered person
beta = 0.3     #possibility of infection
gamma = 0.05   #possibility of recovery
sus = [S]         # #create arrays for storing data
infected = [I]
recovered = [R]
time = [0]      
for t in range(1, 1001):
    contact = beta  * infected[-1] / N       #possibility of contact
    new_infected = np.random.choice(sus[-1], 2, contact)       #select latest S in sus for calculating new infected ones
    new_recovered = np.random.choice(infected[-1], 2, gamma)   #choose one in two as getting infected/recovered or not
    sus_new = sus[-1] - new_infected
    infected_new = infected[-1] + new_infected - new_recovered
    recovered_new = recovered[-1] + new_recovered
    sus.append(sus_new)
    infected.append(infected_new)
    recovered.append(recovered_new)
    time.append(t)
plt.figure(figsize =(6, 4), dpi=150) 
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Model')
plt.plot(time, sus, label='Susceptible', color = 'green')
plt.plot(time, infected, label='Infected', color = 'red')
plt.plot(time, recovered, label='Recovered', color = 'blue')
plt.legend()
plt.savefig('figure', format = 'png')
plt.show()