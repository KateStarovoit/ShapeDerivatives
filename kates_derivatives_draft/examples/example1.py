
#Example 1 meshes
v1, f = igl.read_triangle_mesh(os.path.join(root_folder, "data", "flag.obj"))
v2 = copy.copy(v1)
v2[0] = [-0.1, -0.1,0]
b = np.zeros(len(v1))
b[4] = 1

#L1, L2, M1 and N2
L1 = igl.cotmatrix(v1,f)
L2 = igl.cotmatrix(v2,f)
M1 = igl.massmatrix(v1,f)
M2 = igl.massmatrix(v2,f)
#Solutions to Lu = Mb
sol1 = spsolve(L1, M1*b)
sol2 = spsolve(L2, M2*b)
print("L1 u = M1 b")
print(sol1)
print("L2 u = M2 b")
print(sol2)
#L_grad for firt two triengles
A1 = igl.doublearea(v1,f)
A2 = igl.doublearea(v2,f)
print("L_grad entries for first triangle of v1")
print(grad_li([v1[f[0][0]],v1[f[0][1]],v1[f[0][2]]],A1[0]))
print("L_grad entries for first triangle of v2")
print(grad_li([v2[f[1][0]],v2[f[1][1]],v2[f[1][2]]],A2[0]))
print("L_grad entries for second triangle of v1")
print(grad_li([v1[f[1][0]],v1[f[1][1]],v1[f[1][2]]],A1[1]))
print("L_grad entries for second triangle of v2")
print(grad_li([v2[f[1][0]],v2[f[1][1]],v2[f[1][2]]],A2[1]))
#L_grad assemb;ed for v1 and v2
print("Full l_grad for v1")
print(l_grad(v1,f))
print("Full l_grad for v2")
print(l_grad(v2,f))
#L_grad with respect to x
print("l_grad with respect to x for v1")
print(l_grad_di(v1,f,0))
print("l_grad with respect to x for v2")
print(l_grad_di(v2,f,0))
#L_grad with respect to y
print("l_grad with respect to y for v1")
print(l_grad_di(v1,f,1))
print("l_grad with respect to y for v2")
print(l_grad_di(v2,f,1))
