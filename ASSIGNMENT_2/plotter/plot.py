import matplotlib.pyplot as plt
import csv
def plot(x,y,filename):
    fig = plt.figure()
    plt.plot(x,y,'ro')
    plt.axis([min(x),max(x),min(y),max(y)])

    fig.savefig(filename+".png")
def getLogs(filename):
    vinay_space = []
    with open("../evaluator/logs/"+filename,"r") as f:
        reader = csv.reader(f,delimiter= " " )
        for row in reader:
            newrow = []
            for x in row:
                x = float(x.strip())
                newrow.append(x)
            vinay_space.append(newrow)
    return vinay_space
files = ['traditional']
data = []
for x in files:
    data.append(getLogs(x))
#x = [4,5,6,7,8,9,10,11,12,13,14,15,17,18,19]
#y = [4,5,6,8,9,8,7,8,10,11,8,12,35,20,20]
for j,x in enumerate(data):
    #print(x)
    y = []
    z = []
    for s in x:
        y.append(s[0])
        z.append(s[1])
    print(y[:-2],z[:-2])
    plot(y,z,files[j])
