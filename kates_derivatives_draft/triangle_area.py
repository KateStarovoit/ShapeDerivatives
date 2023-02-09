import torch
import numpy as np

#Area of one triangle
#Input
# V - 3 x 3 tensor of vertex positions
#Output
# a - traingle area
def triangle_area(V):
    s1 = torch.linalg.norm(V[0]-V[1])
    s2 = torch.linalg.norm(V[1]-V[2])
    s3 = torch.linalg.norm(V[2]-V[0])
    p = (s1+s2+s3)/2
    a = torch.sqrt(p*(p-s1)*(p-s2)*(p-s3))
    return a
