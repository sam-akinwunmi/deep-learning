import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    sum_of_exponentials = 0

    for i in range(len(L)):
        sum_of_exponentials += np.exp(i)

    softmax_list = []

    for i in range(len(L)):
    	exp = np.exp(i)
    	exp_to_append = exp / sum_of_exponentials
    	softmax_list.append(exp_to_append)

    return softmax_list