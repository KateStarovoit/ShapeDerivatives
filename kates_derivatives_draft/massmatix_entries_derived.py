import numpy as np

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
            for j in range(3):
                #coordinate
                v0 = v[f[i][j]][k]
                v1 = v[f[i][(j+1)%3]][k]
                v2 = v[f[i][(j+2)%3]][k]
                #edges
                a = np.sqrt(sum(pow(v[f[i][(j+2)%3]] - v[f[i][(j+1)%3]], 2)))
                b = np.sqrt(sum(pow(v[f[i][(j+2)%3]] - v[f[i][j]], 2)))
                c = np.sqrt(sum(pow(v[f[i][(j+1)%3]] - v[f[i][j]], 2)))
                #
                A = (a*a*(2*v0-v1-v2)+(v2-v0)*(b-c*c)+(v1-v0)*(c-b*b))
                B = 2*np.sqrt((a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c))

                M_grad[i][j+k * 3] = A/B

    return(M_grad)
