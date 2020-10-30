import matplotlib.pyplot as plt
import numpy as np

def negative_binomial( k, p ) :
  # Your code to generate a negative_binomial random variable goes here
  
noutcomes =   ##  Variable for the number of bars in your histogram
kparam, prob = 3, 0.8 

# Write the code to repeatedly sample the random variable here and to
# count how often each result comes up in the list called counts here.
# Notice that you will also need to ensure that the heights of all the 
# bars in your histogram sum to one.
counts = np.zeros(noutcomes)



# This part plots the data 
xlabels = np.zeros(noutcomes)
for i in range(noutcomes) : xlabels[i] = kparam + i
plt.bar( xlabels, counts, width=0.1 )
plt.xlabel("Random variable value")
plt.ylabel("Fraction of occurances")
plt.savefig("myhistogram.png")
