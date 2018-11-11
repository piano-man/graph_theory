import math
import cmath
import numpy as np
from plot import plot
R = 100
def getNewNorthPole(dt):
    pi = math.pi
    radian = (pi/180.0)*dt
    sin = math.sin(radian)
    cos = math.cos(radian)
    x = 0
    y = R * sin
    z = R * cos + R
    newNp = (x,y,z)
    return newNp 
def getInput():
    n = input("Enter the number of points")
    n = int(n)
    print("Enter the 2d coordinates of the graph")
    graph = []
    for i in range(n):
        points = input()
        x,y = points.split(" ")
        x = int(x)
        y = int(y)
        z = 0
        graph.append((x,y,z))
    return graph
def getNewCoordinates(point,Np):
    px,py,pz = point 
    x1,y1,z1 = Np

    #writing x and y in terms of x = a1*z+b1 and y = a2 * z + b2
    temp = (x1 - px) / (z1 - pz)
    a1 = temp
    b1 = x1 - ( temp * z1) 

    temp = ( y1 - py ) / ( z1 - pz)
    a2 = temp
    b2 = y1 - (temp * z1)

    alpha = (a1 ** 2) + (a2 ** 2) + 1
    beta = 2*((a1*b1)+(a2*b2)- R )
    c = (b1 * b1) * (b2 * b2)
    a = alpha
    b = beta
    #print(a,b)
    d = (b * b) - (4 * a * c)
    zsol1 = (-b-cmath.sqrt(d))/(2*a)
    zsol2 = (-b+cmath.sqrt(d))/(2*a) 
    za = zsol1.real
    zb = zsol2.real
    znew = 0
    if((za - z1) ** 2 > (zb - z1) ** 2):
        znew = za
    else:
        znew = zb
    xnew = a1 * znew + b1
    ynew = a1 * znew + b2 
    return np.asarray([xnew,ynew,znew])
graph = getInput()
for dt in range(0,90,5):
    newNp = getNewNorthPole(dt) 
    newGraph = []
    for point in graph:
        projectedPoint = getNewCoordinates(point,newNp)
        newGraph.append(projectedPoint)
    newGraph = np.asarray(newGraph)
    #print(np.asarray(newGraph))
    xs = newGraph[:,0]
    ys = newGraph[:,1]
    zs = newGraph[:,2]
    print(xs,ys,zs)
    plot(xs,ys,zs)
    break
