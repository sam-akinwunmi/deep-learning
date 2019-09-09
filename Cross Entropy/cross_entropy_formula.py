import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    return np.sum( ((Y*np.log(P)) + ((np.subtract(1,Y))*np.log(np.subtract(1,P)))) * -1 )