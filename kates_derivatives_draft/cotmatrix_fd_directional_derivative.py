from translate_mesh import *
from cotmatrix import *

'''Input
v - n x 3 list or tensor of vertex positions
f - m x 3 list of faces
d - n x 3 direction for each coordinte of each vertex
h - scalar - magnitude of translation
Output
L_fd - finite difference approximation
  dl/dx:d = lim_{h->0}    (L(x +hd) - L(x))/h
    (L(x+hd) - L(x))//h'''
def cotmatrix_fd_directional_derivative(V, F, d, h):
  V_ = translate_shape(V,d,h)
  L = cotmatrix(V,F)
  L_ = cotmatrix(V_,F)
  return (L_-L)/h
