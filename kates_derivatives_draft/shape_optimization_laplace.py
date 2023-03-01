from torch_lu import *
from gp_torch_utils import *


'''
Optimization using autograd
Input
v - n x 3 vertex positions
f - m x 3 faces
b - 
S - selection matrix s x n
bc - s values(boundary conditions we`re optimizing for)
h - step
n_iter - number of iterations
Output
v_opt - n x 3 optimized ertex positions
'''
def optimize(v, f, b, S, bc, h = 0.01, n_iter = 2):
    v_opt = torch.tensor(v, requires_grad=True)
    solver = LinearDirectSolve.apply
    for _ in range(n_iter):
        L = cotmatrix(v_opt, torch.tensor(f))
        M = mass_matrix(v_opt, torch.tensor(f))
        M_b = torch.sparse.mm(M, b.reshape(b.shape[0],1).double())
        u = solver(L, torch.reshape(M_b,(-1,)))
        E = torch.norm((u@S.double()-bc).sum())
        E.backward()
        E_grad = v_opt.grad
        v_opt = (v_opt.detach() - h*E_grad).requires_grad_(True)
    return v_opt
