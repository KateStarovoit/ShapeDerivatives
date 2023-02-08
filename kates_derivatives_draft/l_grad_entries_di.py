import numpy as np

#returns n*n l_grad_entries matrix
def l_grad_entries_di(v,f,di):
    cot_entries = l_grad_entries(v,f)
    L_grad_assembled = np.zeros((len(f),3))
    for i in range(len(cot_entries)):
        for j in range(len(cot_entries[i])):
            for k in range(len(cot_entries[i][j])):
                 L_grad_assembled [i][j] += cot_entries[i][j][di][k] 
    return L_grad_assembled 
