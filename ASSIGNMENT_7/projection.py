import math
import cmath
import numpy as np
from plot import plot
import matplotlib.pyplot as plt
from animate import animate
R = 100
#!/usr/bin/python

import _thread
import time

# Create two threads as follows
import sys
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
def delete_last_lines(n=1):
    for _ in range(n):
        sys.stdout.write(CURSOR_UP_ONE)
sys.stdout.write(ERASE_LINE)
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
def addEdgesPixels(graph,a,b):
    ax = a[0]
    ay = a[1]
    bx = b[0]
    by = b[1]
    xs = np.linspace(ax,bx,num=100)
    #x-x1/x2-x1 = y - y1 / y2 - y1\
    for x in xs:
        y = (((x-ax)/(bx-ax)) * (by - ay)) + ay
        graph.append(np.asarray([x,y,0]))
    return graph
def getInput():
    n = input("Enter the number of points")
    n = int(n)
    print("Enter the 2d coordinates of the graph")
    graph = []
    vertices = []
    for i in range(n):
        points = input()
        x,y = points.split(" ")
        x = int(x)
        y = int(y)
        z = 0
        graph.append(np.asarray([x,y,z]))
        vertices.append(np.asarray([x,y]))
    vertices = np.asarray(vertices)
    E = input("Enter the number of edges")
    E = int(E)
    print("Enter the edges")
    edges = []
    for i in range(E):
        a,b = input().split(" ")
        a = int(a)
        b = int(b)
        a = vertices[a]
        b = vertices[b]
        edges.append((a,b))
        #graph = addEdgesPixels(graph,a,b)
    graph = np.asarray(graph)
    return graph,vertices,edges
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
    ynew = a2 * znew + b2 
    return np.asarray([xnew,ynew,znew])
def project():  
  graph,vertices,edges = getInput()
  arguments = []
  poles = []
  interval = 1
  for dt in range(0,180,interval):
      mappedPoints =[]
      newNp = getNewNorthPole(dt) 
      poles.append(newNp)
      newGraph = []
      for point in graph:
          projectedPoint = getNewCoordinates(point,newNp)
          newGraph.append(projectedPoint)
          mappedPoints.append((point,projectedPoint))
      newGraph = np.asarray(newGraph)
      #print(np.asarray(newGraph))
      xs = newGraph[:,0]
      ys = newGraph[:,1]
      zs = newGraph[:,2]
      vx = graph[:,0]
      vy = graph[:,1]
      vz = np.zeros(vx.shape)
    #print(xs,ys,zs)
    #print(mappedPoints)
    #plot(xs,ys,zs,vx,vy,vz,mappedPoints,edges)
      arguments.append([xs,ys,zs,vx,vy,vz,mappedPoints,edges])
#fig, ax = plt.subplots()
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  i = 0
  for count,event in enumerate(arguments):
      i += 1
      angle = i * interval
      fig = plt.figure() 
      northpole = poles[i]
      ax = fig.add_subplot(111, projection='3d')
      xs,ys,zs,vx,vy,vz,mappedPoints,edges = event
      plot(xs,ys,zs,vx,vy,vz,mappedPoints,edges,fig,ax,northpole)
      print(str(i)+"/180 completed")
      delete_last_lines()
      fig.savefig("images/"+str(angle)+".png")
      fig.clf()
      plt.close(fig)
#ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                    #init_func=init, blit=True)
#project()
animate()
'''try:
    _thread.start_new_thread(project, () )
    _thread.start_new_thread( animate, () )
except:
    print ("Erearor: unable to start thrd")

while 1:
    pass'''
