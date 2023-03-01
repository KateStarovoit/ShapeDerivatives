import igl
import matplotlib.pyplot as plt
from massmatrix_directional_derivative import *
from massmatrix_fd_directional_derivative import *
from massmatrix_entries_derived import *
#Convergence plots, tests for massmatrix

'''
Compares derived massmatrix to igl
Imput
v - n x 3 vertex positions
f - m x 3 faces
'''
def massmatrix_comparison(v, f):
    M_igl = igl.massmatrix(v,f)
    M = massmatrix(v,f)
    print("Igl\n", M_igl.todense())
    print("Derived\n",M)

'''
Compares finite difference massmatrix directonal derivative to derived
v - n x 3 vertex positions
f - m x 3 faces
d - n x 3 displacements
Prints convergence plot
'''
def fd_byhand(v, f, d):
    h = 1
    x = []
    # compute error
    error = np.zeros(100)
    for i in range(100):
        fd_approximation = massmatrix_fd_directional_derivative(v, f, d, h)
        dir_derivative_approximation = massmatrix_directional_derivative_derived(v, f, d)  #
        error[i] = (abs(fd_approximation - dir_derivative_approximation)).sum()
        x.append(round(h, 4))
        h -= 0.01

    # plot the error
    plt.plot(error)
    plt.ylabel('error')
    plt.xlabel('h')
    plt.xticks(np.arange(len(x)), x)
    plt.ylim(-0.1, 1)
    plt.show()

'''
Compares derieved massmatrix gradient to autograd
Imput
v - n x 3 vertex positions
f - m x 3 faces
d - n x 3 displacements
'''
def entries_comparison(v, f, d):
    # read mesh, set d
    h = 1
    auto_entries = np.round(massmatrix_entries_autograd(v,f),5)
    derived_entries = np.round(massmatrix_entries_derived(v,f),5)
    error = (abs(auto_entries-derived_entries).sum())/(len(f)*9)
    print("entries derived\n", derived_entries)
    print("entries autograd\n", auto_entries)
    print("error\n", round(error,5))


'''
Compares finite difference massmatrix directonal derivative to autograd
v - n x 3 vertex positions
f - m x 3 faces
d - n x 3 displacements
Prints convergence plot
'''
def derivative_comparison(v, f, d):
    h = 1

    x = []
    #compute error
    error = np.zeros(100)
    for i in range(100):
        fd_approximation = massmatrix_fd_directional_derivative(v, f, d, h)
        dir_derivative_approximation = massmatrix_directional_derivative(v, f, d)#
        error[i] = (abs(fd_approximation - dir_derivative_approximation)).sum()
        x.append(round(h,4))
        h -= 0.01

    #plot the error
    plt.plot(error)
    plt.ylabel('error')
    plt.xlabel('h')
    plt.xticks(np.arange(len(x)),x)
    plt.ylim(-0.1,1)
    plt.show()
