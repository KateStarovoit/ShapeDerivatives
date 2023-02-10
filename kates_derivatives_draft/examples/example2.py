import os
from cotmatrix_fd_directional_derivative import *
from cotmatrix_directional_dericative import *

root_folder = os.getcwd()


def example2():
    v, f = igl.read_triangle_mesh(os.path.join(root_folder, "Data", "flag1.obj"))
    b = np.zeros(len(v))
    b[4] = 1
    d = np.zeros((len(v),3))
    d[0] = [0,0,0]
    h = 0.1
    print("fd approximation")
    print(cotmatrix_fd_directional_derivative(v, f, d, h)[0])

    print("directional derivative")
    print(cotmatrix_directional_derivative(v, f, d)[0])
