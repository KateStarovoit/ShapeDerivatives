import torch
from .cotangent_laplacian_intrinsic import cotangent_laplacian_intrinsic
from .halfedge_lengths_squared import halfedge_lengths_squared

#from gpytoolbox
def cotangent_laplacian(V, F):
    """Builds the (pos. def.) cotangent Laplacian for a triangle mesh.
    Parameters
    ----------
    V : (n,d) torch tensor
        vertex list of a triangle mesh
    F : (m,3) torch int array
        face index list of a triangle mesh
    Returns
    -------
    L : (n,n) scipy csr_matrix
        cotangent Laplacian
    Examples
    --------
    TODO

    """

    l_sq = halfedge_lengths_squared(V, F)
    return cotangent_laplacian_intrinsic(l_sq, F, n=V.shape[0])