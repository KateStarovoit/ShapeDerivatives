import torch

#move a vertex x0 along direction v 
def x_e(eps, x0, v):
    return x0 + eps*v
