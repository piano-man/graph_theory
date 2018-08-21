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

def plot(data,filename,lower_limit,upper_limit,isSpace):
	data = np.asarray(data)
	x = data[:,0]
	y = data[:,1]
	z = data[:,2]
	#print(x)
	#print(y)
	#print(z)
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
	ax.set_zlim(lower_limit,upper_limit)

	ax.zaxis.set_major_locator(LinearLocator(10))
	ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

	fig.colorbar(surf, shrink=0.5, aspect=10)
	plt.title(filename)
	if(isSpace):
		filename = "./space/"+filename
	else:
		filename = "./time/"+filename
	fig.savefig(filename+".png")
def getLimits(data):
	vinay_space = data[0]
	gagan_space = data[1]
	vinay_space = np.asarray(vinay_space)
	gagan_space = np.asarray(gagan_space)
	vinay_space = vinay_space[:,2]
	gagan_space = gagan_space[:,2]
	space_max = max(vinay_space.max(),gagan_space.max())
	space_min = min(vinay_space.min(),gagan_space.min())
	
	vinay_time = data[2]
	gagan_time = data[3]
	vinay_time = np.asarray(vinay_time)
	gagan_time = np.asarray(gagan_time)	
	vinay_time = vinay_time[:,2]
	gagan_time = gagan_time[:,2]
	time_max = max(vinay_time.max(),gagan_time.max())
	time_min = min(vinay_time.min(),gagan_time.min())
	return (space_min, space_max,time_min,time_max)
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
#os.system("rm ../evaluator/logs/*")
#os.system("../evaluator/evaluate")
for i in range(4):
	data.append(getLogs(logs[i]))
space_min,space_max,time_min,time_max = getLimits(data)
print(space_min,space_max)
print(time_min,time_max)
for i in range(4):
	if i < 2:
		lower_limit = space_min
		upper_limit = space_max
		isSpace = 1
	else:
		lower_limit = time_min
		upper_limit = time_max
		isSpace = 0

	plot(data[i],logs[i],lower_limit,upper_limit,isSpace)
	
