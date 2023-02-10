from l_grad_entries import *


'''
Input
V - n x 3 vertex positions
F - m x 3 faces
d - n x 3 x 3 directions
Output
n x n cotmatrix directional derivative'''
def cotmatrix_diractional_derivative(v,f,d):
    L_grad = np.zeros((len(v),(len(v))))
    cot_entries = l_grad_entries(v,f)
    for i in range(len(f)):
        for j in range(3):
           entry = 0
           for k in range(len(cot_entries[i][j])):
               for l in range(len(cot_entries[i][j][k])):
                     entry += cot_entries[i][j][k][l] * d[f[i][j]][k]
           L_grad[f[i][(j+1)%3]][f[i][(j+2)%3]]+= entry
           L_grad[f[i][(j+2)%3]][f[i][(j+1)%3]]+= entry
           L_grad[f[i][(j+1)%3]][f[i][(j+1)%3]]-= entry
           L_grad[f[i][(j+2)%3]][f[i][(j+2)%3]]-= entry
    return L_grad
