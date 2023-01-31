import igl
import sys
import torch

sys.path.append('../')
import shape_derivatives_py as shpy

[v, tc, n, f, ftc, fn] = igl.read_obj("./data/fly/fly.obj")
V = torch.tensor(v, requires_grad=True)

F = torch.tensor(f, dtype=torch.long)
[L_torch, i, j, val, tris] = shpy.cotangent_laplacian(V, F)
Vs = V[tris[157]]
# val[0].backward()
torch.autograd.grad(val[157], V, retain_graph=True, )[0][tris[157]]
loss = V.sum()
loss.retain_grad()
loss.backward()


print("hi")
