import numpy as np

"""Step function"""
def step(sum):
    if sum >= 1:
        return 1
    return 0

"""Sigmoide function"""
def sigmoid(sum):
    function = 1 / (1 + (np.exp(-sum)))
    return function

"""Hyperbolic tangent function"""
def hyperbolic_tangent(sum):
    function = (np.exp(sum) - np.exp(-sum)) / (np.exp(sum) + np.exp(-sum))
    return function

"""ReLU function"""
def relu(sum):
    return max(0, sum)

"""Softmax function"""
def softmax(x):
    ex = np.exp(x)    
    return ex / ex.sum()

"""Linear function"""
def linear(soma):   
    return soma

print(relu(2.1))