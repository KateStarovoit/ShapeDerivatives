import igl
import numpy as np


'''l_grad entry for one triangle
Input
v - 3 x 3 triangle vertex positions
A_i - area of corresponding tringle
Output
3 x 3 gradient of triangle
'''
def grad_li(v, A_i):
    grad = np.zeros((3,9))
    for i in range(3):
        k = 0
        for j in range(3):
            grad[i][k  + (i+2)%3] = (v[(i+1)%3][j] - v[(i)%3][j]) / (2*A_i)
            grad[i][k + (i + 1)%3] = (-v[i][j] + v[(i+2)%3][j]) / ( 2*A_i)
            grad[i][k + (i)%3] = (2 * v[(i)%3][j] - v[(i+1)%3][j] - v[(i+2)%3][j]) / ( 2*A_i)
            k += 3
    print(grad)
    return grad

'''l_grad entries for each face
Input
V - n x 3 number of vertex positions
F - m x 3 number of faces
Output
n x 3 list of (3 x 3) gradient for each face
for each of 3 angles of n triangles (3 x 3) entries
'''
def l_grad_entries(v,f):
    L_grad_entries = []
    A = igl.doublearea(v,f)
    for i in range(len(f)):
        L_grad_entries.append(grad_li([v[f[i][0]],v[f[i][1]],v[f[i][2]]],A[i]))
    return L_grad_entries
