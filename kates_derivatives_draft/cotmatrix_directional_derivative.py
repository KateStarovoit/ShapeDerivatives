#directional derivative for cot matrix
'''
TODO: Kate writes input and output
'''
def cotmatrix_directional_derivative(v, f, d):
    L_grad = np.zeros((len(v),(len(v))))
    dcotijdx = l_grad_entries_di(v,f,0)
    dcotijdy = l_grad_entries_di(v,f,1)
    dcotijdz = l_grad_entries_di(v,f,2)
    dcotij = [dcotijdx , dcotijdy ,dcotijdz]
    
    for i in range(len(f)):
        for j in range(3):
            for k in range(3):
               entry = dcotij[k][i][j]*d[i][j][k]
               L_grad[f[i][(j+1)%3]][f[i][(j+2)%3]]+= entry
               L_grad[f[i][(j+2)%3]][f[i][(j+1)%3]]+= entry
               L_grad[f[i][(j+1)%3]][f[i][(j+1)%3]]-= entry
               L_grad[f[i][(j+2)%3]][f[i][(j+2)%3]]-= entry
    return L_grad
