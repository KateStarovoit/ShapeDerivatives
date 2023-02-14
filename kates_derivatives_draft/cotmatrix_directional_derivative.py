from l_grad_entries import *

'''
Input
V - n x 3 vertex positions
F - m x 3 faces
d - n x 3 x 3 directions
Outputx
n x n cotmatrix directional derivative'''
def cotmatrix_directional_derivative(v,f,d):
    L_grad = np.zeros((len(v),(len(v))))
    cot_entries = l_grad_entries(v,f)

    for i in range(len(f)):
        for j in range(3):
           d_ = np.zeros(9)
           for k in range(3):
               for l in range(3):
                    d_[k+(l*3)] = d[f[i][(k-j)%3]][l]
           entry = sum(cot_entries[i][j]*d_)
           L_grad[f[i][(j+1)%3]][f[i][(j+2)%3]]+= entry
           L_grad[f[i][(j+2)%3]][f[i][(j+1)%3]]+= entry
           L_grad[f[i][(j+1)%3]][f[i][(j+1)%3]]-= entry
           L_grad[f[i][(j+2)%3]][f[i][(j+2)%3]]-= entry
    return L_grad
