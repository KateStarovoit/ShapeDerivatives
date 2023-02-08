import torch

#Gradient of the mass matrix
def m_grad(v,f):
    M_grad = []
    for fi in f:
         M_grad.append(torch.autograd.functional.jacobian(area,torch.tensor([v[fi[0]],v[fi[1]],v[fi[2]]])))
    return(M_grad)
