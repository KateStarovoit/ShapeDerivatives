import numpy as np
from triangle_area import *

'''massmatrix entries computed by autpgrad
Input
V - n x 3 number of vertex positions
F - m x 3 number of faces
Output
list of (3 x 3) gradient for each face
'''
def massmatrix_entries_autograd(v,f):
    M_grad = np.zeros((len(f),9))
    for i in range(len(f)):
        mi = torch.autograd.functional.jacobian(triangle_area,torch.tensor([v[f[i][0]],v[f[i][1]],v[f[i][2]]]))
        for j in range(3):
            for k in range(3):
                M_grad[i][j + k * 3] = mi[j][k]
    return(M_grad)

'''massmatrix entries computed by formulas derived by hand
Input
V - n x 3 number of vertex positions
F - m x 3 number of faces
Output
list of (3 x 3) gradient for each face
'''
def massmatrix_entries_derived(v,f):
    M_grad = np.zeros((len(f),9))
    for i in range(len(f)):
        for k in range(3):
            #current coords
            v0 = v[f[i][0]][k]
            v1 = v[f[i][1]][k]
            v2 = v[f[i][2]][k]
            #current edges
            a = np.sqrt(sum(pow(v[f[i][2]] - v[f[i][1]], 2)))
            b = np.sqrt(sum(pow(v[f[i][2]] - v[f[i][0]], 2)))
            c = np.sqrt(sum(pow(v[f[i][1]] - v[f[i][0]], 2)))
            p = (a+b+c)/2
            #
            A = a*a*(v1-v2)+(v2-v0)*(b-c*c)+(v1-v0)*(c-b*b)
            B = np.sqrt(2*p*(p-a)*(p-b)*(p-c))
            print("A1 ", A)
            M_grad[i][k * 3] = A/B
            #
            A = -b*b*(v2-v0)+(v2-v1)*(c*c-a)+(v1-v0)*(a*a-c)
            print("A2 ", A)
            M_grad[i][k * 3 + 1] = A/B
            #
            A = c*c*(2*v2-v0-v1)+(v2-v0)*(a-b*b)+(v2-v1)*(b*b-a)
            print("A3 ", A)
            print("B ", B)
            B_ = 0
            print("B_ ", B_)
            M_grad[i][k * 3 + 2] = A / B
    return(M_grad)
