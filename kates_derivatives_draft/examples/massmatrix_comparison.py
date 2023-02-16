import matplotlib.pyplot as plt
from massmatrix_directional_derivative import *
from massmatrix_fd_directional_derivative import *
import igl

def massmatrix_comparison(v, f):
    M_igl = igl.massmatrix(v,f)
    M = massmatrix(v,f)
    print("Igl\n", M_igl.todense())
    print("Derived\n",M)

def entries_comparison(v, f, d):
    # read mesh, set d
    error = np.zeros(5)
    x = []
    h = 0.1
    for i in range(1):
        auto_entries = np.round(massmatrix_entries_autograd(v,f),10)
        derived_entries = massmatrix_entries_derived(v,f)
        error[i] = abs(auto_entries-derived_entries).sum()
        print("entries derived\n", derived_entries)
        print("entries autograd\n", auto_entries)
        print("error\n", error[i])
        v = translate_shape(v,d,h)
        h *= 2
        x.append(round(h, 4))
    #plt.plot(error)
    #plt.ylabel('error')
    #plt.xlabel('h')
    #plt.xticks(np.arange(len(x)),x)
    #plt.show()

def derivative_comparison(v, f, d):
    h = 1

    x = []
    #compute error
    error = np.zeros(10)
    for i in range(10):
        fd_approximation = massmatrix_fd_directional_derivative(v, f, d, h)
        dir_derivative_approximation = massmatrix_directional_derivative(v, f, d)#
        error[i] = (abs(fd_approximation - dir_derivative_approximation)).sum()
        x.append(round(h,4))
        h /= 2

    #plot the error
    plt.plot(error)
    plt.ylabel('error')
    plt.xlabel('h')
    plt.xticks(np.arange(len(x)),x)
    plt.ylim(-0.1,1)
    plt.show()
