'''Translates v along direction d
Input
v - n x 3 list or torch.tensor of vertex positions
d - n x 3 direction for each coordinte of each vertex
h - scalar - magnitude of translation
Output
n x 3 translated vertex positions'''
def translate_shape(V,d,h):
  return V + d*h
