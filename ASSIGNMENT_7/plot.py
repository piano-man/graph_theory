# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np
def plot(xs,ys,zs):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xs, ys, zs, c='r', marker='o')

    u = np.linspace(0, 2 * np.pi, 13)
    v = np.linspace(0, np.pi, 13)

    x = 100 * np.outer(np.cos(u), np.sin(v))
    y = 100 * np.outer(np.sin(u), np.sin(v))
    z = 100 * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, rstride=1, cstride=1, color='w', shade=0)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()
