#directional derivative for cot matrix
'''
Input
V - n x 3vertex positions
F - m x 3 faces
d - n x n direction matrix
Output
n x n cotmatrix directional derivative
'''
def cotmatrix_directional_derivative(V, F, d):
    L_grad = l_grad(v,f)
    print(len(L_grad), len(d))
    for i in range(len(v)):
        for j in range(len(v)):
            L_grad[i][j] *= d[i][j]
    return L_grad
