import torch
#comes from gpytoolbox implementation, adapted to torch
def doublearea_intrinsic(l_sq,F):
    """Construct the doublearea of each element of a line or triangle mesh.
    Parameters
    ----------
    l_sq : (m,3) torch tensor
        squared halfedge lengths as computed by halfedge_lengths_squared
    F : (m,3) torch tensor
        face index list of a triangle mesh
    Returns
    -------
    dblA : (m,) torch tensor
        vector of twice the (unsigned) area/length
    See Also
    --------
    doublearea.
    Examples
    --------
    TO-DO
    """

    assert F.shape == l_sq.shape
    assert F.shape[1]==3
    assert torch.all(l_sq >= 0)

    l = torch.sqrt(l_sq)

    # Using Kahan's formula
    # https://people.eecs.berkeley.edu/~wkahan/Triangle.pdf
    a,b,c = l[:,0], l[:,1], l[:,2]
    dblA = 0.5 * torch.sqrt((a+(b+c)) * (c-(a-b)) * (c+(a-b)) * (a+(b-c)))

    return dblA