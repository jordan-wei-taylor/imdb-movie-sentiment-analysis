import numpy as np

def accuracy(y, y_hat):
    return (y == y_hat).mean()

def recall(y, y_hat):
    c   = len(np.unique(y))
    ret = np.zeros(c)
    for i in range(c):
        ret[i] = (y_hat[y == i] == i).mean()
    return ret
