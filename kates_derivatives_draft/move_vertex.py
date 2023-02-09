import torch

#move a vertex x0 along direction v 
#Input
#eps - scalar magnitude of translation
#v - n x 3 tensor that gives direction
#x0 - n x 3 tensor of vertex position
def x_e(eps, x0, v):
    return x0 + eps*v
