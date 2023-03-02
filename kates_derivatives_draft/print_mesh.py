import polyscope as ps
import numpy as np

'''
Prints a mesh
Input
v - n x 3 vertex positions
f - m x 3 triangle faces
'''
def print_mesh(v,f):
    ps.init()
    ps.register_surface_mesh("shape", v, f)
    ps.show()

'''
Prints a mesh and solution as colormap
Input
v - n x 3 vertex positions
f - m x 3 triangle faces
u - n x 1 array of solution quantities
'''
def print_solution(v,f,u):
    ps.init()
    shape = ps.register_surface_mesh("shape", v, f)
    ps.SurfaceMesh.add_scalar_quantity(shape, "values", np.array(u))
    ps.show()

'''
Prints a mesh and solutions as colormap
Input
v - n x 3 vertex positions
f - m x 3 triangle faces
u - n x 1 array of solution quantities
'''
def print_solutions(v,f,u):
    ps.init()
    shape = ps.register_surface_mesh("shape", v, f)
    for i in range(len(u)):
        ps.SurfaceMesh.add_scalar_quantity(shape, f"values {i}", np.array(u[i]))
    ps.show()
