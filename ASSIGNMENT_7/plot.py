# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np
def plot(xs,ys,zs,vx,vy,vz,mappedPoints,edges,fig,ax,northpole):
    #fig = plt.figure()
    #ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xs, ys, zs, c='#000000', marker='o')
    ax.scatter(vx,vy,vz,c='b',marker='^')
    
    '''u = np.linspace(0, 2 * np.pi, 13)
    v = np.linspace(0, np.pi, 13)

    x = 100 * np.outer(np.cos(u), np.sin(v))
    y = 100 * np.outer(np.sin(u), np.sin(v))
    z = 100 * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, rstride=1, cstride=1, color='w', shade=0)
    '''
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    zoom = 1.5
    for edge in edges:
        point1,point2 = edge
        xs = []
        ys = []
        zs = []
        xs.append(point1[0])
        xs.append(point2[0])
        ys.append(point1[1])
        ys.append(point2[1])
        zs.extend([0,0])
        ax.plot(xs,ys,zs,'b')
    #plt.show()
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)

    x = 100 * np.outer(np.cos(u), np.sin(v))
    y = 100 * np.outer(np.sin(u), np.sin(v))
    z = 100 * np.outer(np.ones(np.size(u)), np.cos(v)) + 100
#for i in range(2):
#    ax.plot_surface(x+random.randint(-5,5), y+random.randint(-5,5), z+random.randint(-5,5),  rstride=4, cstride=4, color='b', linewidth=0, alpha=0.5)
    elev = 10.0
    rot = 80.0 / 180 * np.pi
    ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b', linewidth=0, alpha=0.5)
#calculate vectors for "vertical" circle
    a = np.array([-np.sin(elev / 180 * np.pi), 0, np.cos(elev / 180 * np.pi)])
    b = np.array([0, 1, 0])
    b = b * np.cos(rot) + np.cross(a, b) * np.sin(rot) + a * np.dot(a, b) * (1 - np.cos(rot))
    ax.plot(np.sin(u),np.cos(u),0,color='k', linestyle = 'dashed')
    horiz_front = np.linspace(0, np.pi, 100)
    ax.plot(np.sin(horiz_front),np.cos(horiz_front),0,color='k')
    vert_front = np.linspace(np.pi / 2, 3 * np.pi / 2, 100)
    ax.plot(a[0] * np.sin(u) + b[0] * np.cos(u), b[1] * np.cos(u), a[2] * np.sin(u) + b[2] * np.cos(u),color='k', linestyle = 'dashed')
    ax.plot(a[0] * np.sin(vert_front) + b[0] * np.cos(vert_front), b[1] * np.cos(vert_front), a[2] * np.sin(vert_front) + b[2] * np.cos(vert_front),color='k')

    polex,poley,polez = northpole
    #ax.view_init(elev = elev, azim = 0)
    ax.set_xlim([-150*zoom,150*zoom])
    ax.set_ylim([-150*zoom,150*zoom])
    ax.set_zlim([0*zoom,200*zoom])
    for point,projection in mappedPoints:
        xs = []
        ys = []
        zs = []
        xs.append(point[0])
        #xs.append(projection[0])
        xs.append(polex)
        ys.append(point[1])
        #ys.append(projection[1])
        ys.append(poley)
        zs.append(point[2])
        #zs.append(projection[2])
        zs.append(polez)
        ax.plot(xs,ys,zs,'r--')
    return ax
