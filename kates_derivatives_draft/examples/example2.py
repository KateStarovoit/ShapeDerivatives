v, f = igl.read_triangle_mesh(os.path.join(root_folder, "data", "flag.obj"))
b = np.zeros(len(v))
b[4] = 1
d = np.zeros((len(v),3))
d[0] = [-1,0,0]
h = 0.1
print("fd approximation")
print(cotmatrix_fd_directional_derivative(v, f, d, h))
d = np.ones((len(v),len(v)))
d[0][0] = -1
print("directional derivative")
print(cotmatrix_directional_derivative(v, f, d))
