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
# put the data into a pandas DataFrame (this is what my data looks like)

def plot(data,filename):
	data = np.asarray(data)
	x = data[:,0]
	y = data[:,1]
	z = data[:,2]
	print(x)
	print(y)
	print(z)
	xyz = {'x': x, 'y': y, 'z': z}
	df = pd.DataFrame(xyz, index=range(len(xyz['x'])))
	# re-create the 2D-arrays
	x1 = np.linspace(df['x'].min(), df['x'].max(), len(df['x'].unique()))
	y1 = np.linspace(df['y'].min(), df['y'].max(), len(df['y'].unique()))
	x2, y2 = np.meshgrid(x1, y1)
	z2 = griddata((df['x'], df['y']), df['z'], (x2, y2), method='cubic')

	fig = plt.figure()
	ax = fig.gca(projection='3d')
	surf = ax.plot_surface(x2, y2, z2, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
	ax.set_zlim(z.min(),z.max())

	ax.zaxis.set_major_locator(LinearLocator(10))
	ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

	fig.colorbar(surf, shrink=0.5, aspect=5)
	plt.title(filename)
    # ~~~~ MODIFICATION TO EXAMPLE ENDS HERE ~~~~ #

	#plt.show()
	fig.savefig(filename+".png")
def getLogs(filename):
	vinay_space = []
	with open("../evaluator/logs/"+filename,"r") as f:
		reader = csv.reader(f,delimiter= " " );
		for row in reader:
			newrow = []
			for x in row:
				x = float(x)
				newrow.append(x)
			vinay_space.append(newrow);
	return vinay_space
logs = ["vinay_space","gagan_space","vinay_time","gagan_time"]
data = []
for files in logs:
	data = getLogs(files)
	print(data[0])
	plot(data,files)
