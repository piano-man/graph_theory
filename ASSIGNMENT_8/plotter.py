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
import random
from math import log10 as log
fig = plt.figure()
ax = fig.gca(projection='3d')
#surf = ax.plot_surface(x2, y2, z2, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
ax.set_zlim(lower_limit,upper_limit)
ax.set_xlabel("Number of Edges, m " )
ax.set_ylabel("Number of Vertices, n")
ax.set_zlabel("Time taken in micro seconds")
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.2f'))
#fig.colorbar(surf, shrink=0.5, aspect=10)
def plot(x,y,z,x3,y3,z3,filename,upper_limit,lower_limit):
	#lower_limit = z.min()
	#upper_limit = z.max()
	xyz = {'x': x, 'y': y, 'z': z}
	df = pd.DataFrame(xyz, index=range(len(xyz['x'])))
	x1 = np.linspace(df['x'].min(), df['x'].max(), len(df['x'].unique()))
	y1 = np.linspace(df['y'].min(), df['y'].max(), len(df['y'].unique()))
	x2, y2 = np.meshgrid(x1, y1)
	z2 = griddata((df['x'], df['y']), df['z'], (x2, y2), method='cubic')
	ax = fig.gca(projection='3d')
	surf = ax.plot_surface(x2, y2, z2, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
	#ax.set_zlim(lower_limit,upper_limit)
	#ax.set_xlabel("Number of Edges, m " )
	#ax.set_ylabel("Number of Vertices, n")
	#ax.set_zlabel("Time taken in micro seconds")
	#ax.zaxis.set_major_locator(LinearLocator(10))
	#ax.zaxis.set_major_formatter(FormatStrFormatter('%.2f'))
	fig.colorbar(surf, shrink=0.5, aspect=10)
	plt.title(filename)
	fig.savefig(filename+".png")
total = 100
x = np.linspace(0,total,total)
y = np.linspace(0,total,total)
dataset = []
dataset2 = []
count = 0
total = x.shape[0]**2
for i in range(x.shape[0]):
	for j in range(y.shape[0]):
		print("Completed "+str(count)+"/"+str(total))
		z = x[i] * y [j]
		try:
			z2 = log(y[j])
		except:
			z2 = 0
		errPercentage = float(random.randint(1,100))/100.
		err = z * errPercentage * 0.217
		err2 = z2 * errPercentage * 0.217
		sign = random.randint(0,2)
		if(sign == 1):
			err *= -1
		
		dataset.append([x[i],y[j],z + err])
		dataset2.append([x[i],y[j],z2 + err2])
		count += 1
dataset = np.asarray(dataset)
x = dataset[:,0]
y = dataset[:,1]
z = dataset[:,2]
#plot(x,y,z,"hello")
dataset2 = np.asarray(dataset2)
x2 = dataset2[:,0]
y2 = dataset2[:,1]
z2 = dataset2[:,2]
upper = max(z2.max(),z.max())
lower = min(z2.min(),z.min())
#plot(x,y,z,"simple",upper,lower)
plot(x,y,z,x2,y2,z2,"complex",upper,lower)
