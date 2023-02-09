#Computes n x n l_grad for directional derivative
'''
Input
V - n x 3 vertex positions
F - m x 3 faces
Output
n x n cotmatrix grad matrix
'''
def l_grad(v,f):
    L_grad = np.zeros((len(v),(len(v))))
    cot_entries = l_grad_entries_assembled(v,f)
    print(len(cot_entries))
    for i in range(len(f)):
        for j in range(3):
           L_grad[f[i][(j+1)%3]][f[i][(j+2)%3]]+= cot_entries[i][j]
           L_grad[f[i][(j+2)%3]][f[i][(j+1)%3]]+= cot_entries[i][j]
           L_grad[f[i][(j+1)%3]][f[i][(j+1)%3]]-= cot_entries[i][j]
           L_grad[f[i][(j+2)%3]][f[i][(j+2)%3]]-= cot_entries[i][j]
    return L_grad
