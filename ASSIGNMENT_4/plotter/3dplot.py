from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import re
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import os

def plot(data,filename):
    data = np.asarray(data)
    x = data[:,0]
    y = data[:,1]
    z = data[:,2]
    print(x)
    print(y)
    print(z)
    print(filename,z.min(),z.max())
    xyz = {'x': x, 'y': y, 'z': z}
    df = pd.DataFrame(xyz, index=range(len(xyz['x'])))
    x1 = np.linspace(df['x'].min(), df['x'].max(), len(df['x'].unique()))
    y1 = np.linspace(df['y'].min(), df['y'].max(), len(df['y'].unique()))
    x2, y2 = np.meshgrid(x1, y1)
    z2 = griddata((df['x'], df['y']), df['z'], (x2, y2), method='cubic')
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(x2, y2, z2, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
    ax.set_zlim(z.min(),z.max())
    print(z.min(),z.max())
    ax.zaxis.set_major_locator(LinearLocator(10))
    #ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    fig.colorbar(surf, shrink=0.5, aspect=10)
    plt.xlabel("Vertices")
    plt.ylabel("Edges")
    plt.legend()
    plt.title(filename)
    fig.savefig(filename+".png")
def getLogs(filename):
    vinay_space = []
    with open(filename,"r") as f:
        reader = csv.reader(f,delimiter= " " )
        for row in reader:
            newrow = []

            for count,x in enumerate(row):
                if(count == 0):
                    continue
                x = float(x)
                newrow.append(x)
                vinay_space.append(newrow)
    return vinay_space
data = []
data = getLogs("../evaluator/ymw.txt");
print(data)
plot(data,"backtrack")
