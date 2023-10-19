import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# Linear congruential generator
# si+1 = (a* si + c) mod m

n = int(input('Enter number of random number required:'))
initial = 12
m = 101
c = 17
a = 79
res = [initial]

while len(res)-1!=n:
    si = (a*initial+c)%m
    res.append(si)
    initial = si
    
#print('Resultant random number --> ',res)
plt.hist(res)
plt.show()

# Lagged Fibonacci generator
j,k=3,5
m=100
seed = list('6421893')
res=[]
while len(res)!=n:
    si = int(seed[j])*(int(seed[k]))%m
    res.append(si)
    seed.pop(0)
    seed.append(str(si))
#print('Resultant random number --> ',res)
plt.hist(res)
sns.distplot(res)
plt.show()

# Blum Blum Shub
res =[]
x0=8345
m=101
while len(res)!=n:
    xi = (pow(x0,2,m))
    x0 = xi
    res.append(xi)
#print('Resultant random number --> ',res)
plt.hist(res)
plt.show()

# Linear-feedback shift register
start_state = 1 << 15 | 1
lfsr = start_state
res = []

while len(res)-1!=n:
    bit = (lfsr ^ (lfsr >> 1) ^ (lfsr >> 3) ^ (lfsr >> 12)) & 1
    lfsr = (lfsr >> 1) | (bit << 15)
    res.append(lfsr)
#print('Resultant random number --> ',res)
plt.hist(res)
plt.show()

def normal_poisson_uniform():

    def normalDistributionRandomNumber():
        normalRand = np.random.normal(5000,2000,5000)
        plt.hist(normalRand,label="NORMAL")
        plt.show()

    def poissonDistributionRandomNumber():
        poissonRand = np.random.poisson(100,5000)
        plt.hist(poissonRand,label="POISSON")
        plt.show()
        
    def uniformDistributionRandomNumber():
        uniformRand = np.random.uniform(10,100,5000)
        plt.hist(uniformRand,label="UNIFORM")
        plt.show()
        
    def exponentialDistributionRandomNumber():
        expRand = np.random.exponential(scale=4,size=10)
        plt.hist(expRand,label="Exponential")
        plt.show()
        
    normalDistributionRandomNumber()
    poissonDistributionRandomNumber()
    uniformDistributionRandomNumber()
    exponentialDistributionRandomNumber()