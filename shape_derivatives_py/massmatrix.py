import torch
import scipy as sp


def massmatrix(V, F):
    """
    builds the mass matrix with pytorch in order to backpropagate through its entries
    Inputs:
        V: #Vx3 vertices of the mesh
        F: #Fx3 faces of the mesh
    Outputs:
        M: mass matrix (scipy sparse matrix)
        i: row indices of the mass matrix (torch tensor)
        j: column indices of the mass matrix (torch tensor)
        v: values of the mass matrix (torch tensor)
    """
    i = []
    j = []
    v = []
    for i in range(F.shape[0]):
        # get all edge lengths
        e1 = V[F[i, 2], :] - V[F[i, 1], :]
        e2 = V[F[i, 0], :] - V[F[i, 2], :]
        e3 = V[F[i, 1], :] - V[F[i, 0], :]

        l1 = torch.norm(e1, dim=1)
        l2 = torch.norm(e2, dim=1)
        l3 = torch.norm(e3, dim=1)

        s = (l1 + l2 + l3) / 2  # semiperimeter
        A = torch.sqrt(s * (s - l1) * (s - l2) * (s - l3))  # Area using Heron's formula
        ii = [F[i, 0], F[i, 1], F[i, 2]]
        jj = [F[i, 0], F[i, 1], F[i, 2]]
        vv = [A/2, A/2, A/2]
        i.extend(ii)
        j.extend(jj)
        v.extend(vv)

    M = sp.sparse.csc_matrix((v, (i, j)), shape=(V.shape[0], V.shape[0]))
    return M, i, j, v