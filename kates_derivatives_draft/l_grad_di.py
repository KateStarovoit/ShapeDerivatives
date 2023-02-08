#l_grad in one direction(dx, dy or dz)
def l_grad_di(v,f,di):
    L_grad = np.zeros((len(v),(len(v))))
    cot_entries = l_grad_entries_di(v,f,di)
    for i in range(len(f)):
        for j in range(3):
           L_grad[f[i][(j+1)%3]][f[i][(j+2)%3]]+= cot_entries [i][j]
           L_grad[f[i][(j+2)%3]][f[i][(j+1)%3]]+= cot_entries [i][j]
           L_grad[f[i][(j+1)%3]][f[i][(j+1)%3]]-= cot_entries [i][j]
           L_grad[f[i][(j+2)%3]][f[i][(j+2)%3]]-= cot_entries [i][j]
    return L_grad
