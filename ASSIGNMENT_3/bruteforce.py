n = 0
import numpy as np
from itertools import permutations
from os import system
from time import time
from time import sleep
import pickle as pkl
def log(n,t):
    f = open("logs/bruteforce","a")
    f.write(str(n)+" "+ str(t)+"\n")
def createRandomMatrix(n):
    a = permutations(range(n))
    fact = 1
    for i in range(1,n+1):
        fact *= i
        print(fact)
    l = fact/ 2
    count = 0
    per = []
    for x in a:
        count += 1
        if(count == l):
            break
        per = x
    print(l)
    mat = np.zeros((n,n))
    for i in range(n-1):
        mat[per[i]][per[i+1]] = 1
        mat[per[i]][per[i+1]] = 1
    return mat
def makeHamiltonian(mat):
    n = len(mat)
    visited = []
    count = n
    first = 0
    for i in range(n):
        r = np.random.randint(count)
        mat[first][r] = 1
        first = r
        count -= 1
    return mat
def checkIfValid(mat,pattern):
    for i in range(len(pattern)-1):
        x = pattern[i]
        y = pattern[i+1]
        if(mat[x][y] == 0 and mat[y][x] == 0):
            return False
    return True
def checkIfHamiltonian(n,a):
    #a = permutations(range(n))
    mat = createRandomMatrix(n)
    isHamiltonian = False
    #print(mat)
    #mat = makeHamiltonian(mat)

    t = time()
    count =0
    for pattern in a:
        if(checkIfValid(mat,pattern)):
            isHamiltonian = True
            print("This is a Hamiltonian Path")
            count += 1
            print(count)
            break
        else:
            continue
    if(not isHamiltonian):
        print("Not a Hamiltonian")
    t = time() - t
    return t
system("rm -rf logs/*")
perms = pkl.load(open("permutations.pkl","rb"))
for i in range(4,20):
    t = checkIfHamiltonian(i,perms[i])
    log(i,t)
    print(i,t)
    if ( t > 1):
        print("Breaking number:",i)
        break
