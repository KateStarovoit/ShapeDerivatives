import numpy as np
import scipy as sp
from .cotangent_weights_intrinsic import cotangent_weights_intrinsic
import torch

#from gpytoolbox
def cotangent_laplacian_intrinsic(l_sq, F, n=None):
    """Builds the (pos. def.) cotangent Laplacian for a triangle mesh.
    Parameters
    ----------
    l_sq : (m,3) numpy array
        squared halfedge lengths as computed by halfedge_lengths_squared
    F : (m,3) numpy int array
        face index list of a triangle mesh
    n : int, optional (default None)
        number of vertices in the mesh.
        If absent, will try to infer from F.
    Returns
    -------
    L : (n,n) scipy csr_matrix
        cotangent Laplacian
    rows : (m,3) numpy int array
        row indices of the Laplacian
    cols : (m,3) numpy int array
        column indices of the Laplacian
    vals : (m,3) numpy float array
        values of the Laplacian
    Examples
    --------
    ```python
    # Mesh in V,F
    from gpytoolbox import halfedge_lengths_squared, cotangent_laplacian_intrinsic
    l = halfedge_lengths_squared(V,F)
    L = cotangent_laplacian_intrinsic(l_sq,F,n=V.shape[0])
    ```

    """

    assert F.shape[1] == 3
    assert l_sq.shape == F.shape


    if n == None:
        n = torch.max(F) + 1

    C = cotangent_weights_intrinsic(l_sq, F)

    rows = torch.cat((F[:, 0], F[:, 1], F[:, 1], F[:, 2], F[:, 2], F[:, 0],
                           F[:, 0], F[:, 1], F[:, 2]))
    cols = torch.cat((F[:, 1], F[:, 0], F[:, 2], F[:, 1], F[:, 0], F[:, 2],
                           F[:, 0], F[:, 1], F[:, 2]))

    tris = torch.tile(F, (9, 1))
    data = torch.cat((-C[:, 2], -C[:, 2], -C[:, 0], -C[:, 0], -C[:, 1], -C[:, 1],
                           C[:, 1] + C[:, 2], C[:, 2] + C[:, 0], C[:, 0] + C[:, 1]))



    L = sp.sparse.csr_matrix((data.detach().numpy(), (rows.detach().numpy(), cols.detach().numpy())),
                             shape=(n, n))

    return L, rows, cols, data, tris