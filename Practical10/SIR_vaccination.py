import numpy as np 
import matplotlib.pyplot as plt 
N = 10000
I = 1
S = N - I 
R = 0
beta = 0.3
gamma = 0.05
vaccine_rate = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
def vaccination(v_rate): #make former steps together a function,so that it's more convenient to test with different vaccination rates
    S = N * (1 - v_rate)  #vaccinated ones don't get infected
    I= 1  
    R = 0
    sus = [S]
    infected = [I]
    recovered = [R]
    time = [0]
    for t in range(1, 1001):
        contact = beta * infected[-1] / N
        new_infected = np.random.binomial(sus[-1], contact)  #r.binomial(x,p) = r.choice(x,2,p)
        new_recovered = np.random.binomial(infected[-1], gamma)
        sus_new = sus[-1] - new_infected
        infected_new = infected[-1] + new_infected - new_recovered
        recovered_new = recovered[-1] + new_recovered
        sus.append(sus_new)
        infected.append(infected_new)
        recovered.append(recovered_new)
        time.append(t)
    return time, infected #return these two values to draw the new figure
for v_rate in vaccine_rate:
    newtime, newI = vaccination(v_rate)
    plt.plot(newtime, newI,label = v_rate)
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Model with Different Vaccination Rates')
plt.legend()
plt.savefig('infections_under_vaccination_rates.png', format='png')
plt.show()