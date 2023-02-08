import igl
import numpy as np

mesh_name = "bunny.obj" #[also do other meshes]
[V, F] = igl.read_obj("data" + "/" + mesh_name ".obj")
h = 1e-3
A_fd = cotmatrix_fd_directional_derivative(V, F, h, D)
A = cotmatrix_directional_derivative(V, F, D)

# A_fd should be very similar to A, and should get closer to A as h becomes smaller

# To finish the test, loop through different values of h = [1, 1e-1, 1e-2 ... 1e-15]


# plot the error between A and A_fd for each value of h. 
# error = np.linalg.norm((A - A_fd).todense())
# plot above error with h





