import torch

#Gradient of the mass matrix
#Input
#V - n x 3 list or tensor of vertex positions
#F - m x 3 ist or tensor of faces
#Output
#Mass matrix gradient
def m_grad(v,f):
    M_grad = []
    for fi in f:
         M_grad.append(torch.autograd.functional.jacobian(area,torch.tensor([v[fi[0]],v[fi[1]],v[fi[2]]])))
    return(M_grad)
