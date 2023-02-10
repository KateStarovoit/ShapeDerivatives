import igl
import numpy as np
import trig

'''Same as libigl cotmatrix. Computes Laplace matrix for a mesh
Input
V - n x 3 - list of vertex positions
F - m x 3 - list of faces
Output
n x n - Laplace matrix'''
def cotmatrix(v, f):
    l = igl.edge_lengths(v,f)
    A = igl.doublearea(v,f)
    cot = np.zeros((len(l),3))
    for i in range(len(l)):
        cot[i] = trig.find_cot(l[i][0], l[i][1], l[i][2], A[i])
    L = np.zeros((len(v),(len(v))))
    for i in range(len(l)):
        for j in range(3):
           L[f[i][(j+1)%3]][f[i][(j+2)%3]]+= cot[i][j]
           L[f[i][(j+2)%3]][f[i][(j+1)%3]]+= cot[i][j]
           L[f[i][(j+1)%3]][f[i][(j+1)%3]]-= cot[i][j]
           L[f[i][(j+2)%3]][f[i][(j+2)%3]]-= cot[i][j]
    return L
