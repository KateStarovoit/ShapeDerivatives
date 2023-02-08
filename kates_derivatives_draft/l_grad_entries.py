import igl
import numpy as np

#l_grad for one triangle
def grad_li(v,A_i):
    grad = [np.zeros((3,3)), np.zeros((3,3)), np.zeros((3,3))]
    for i in range(len(grad)):
        for j in range(0,3):
            grad[i][j][0] = (2*v[i%3][j]-v[(i+1)%3][j]-v[(i+2)%3][j])/(4*A_i)
            grad[i][j][1] = (v[(i+2)%3][j]-v[i%3][j])/(4*A_i)
            grad[i][j][2] = (-v[(i+1)%3][j]-v[i%3][j])/(4*A_i)
    return grad

#l_grad entries for each face
def l_grad_entries(v,f):
    L_grad_entries = []
    A = igl.doublearea(v,f)
    for i in range(len(f)):
        L_grad_entries.append(grad_li([v[f[i][0]],v[f[i][1]],v[f[i][2]]],A[i]))
    return L_grad_entries

#returns n*n l_grad_entries matrix
def l_grad_entries_assembled(v,f):
    cot_entries = l_grad_entries(v,f)
    L_grad_assembled = np.zeros((len(f),3))
    for i in range(len(cot_entries)):
        for j in range(len(cot_entries[i])):
            for k in range(len(cot_entries[i][j])):
                for l in range(len(cot_entries[i][j][k])):
                      L_grad_assembled [i][j] += cot_entries[i][j][k][l] 
    return L_grad_assembled 
