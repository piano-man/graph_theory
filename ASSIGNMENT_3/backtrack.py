# Python program for solution of
# hamiltonian cycle problem
from time import time
import numpy as np
from itertools import permutations
def log(n,t):
    f = open("logs/backtrack","a")
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
    mat[per[n-1]][0] = 1
    mat[0][per[n-1]]
    return mat
class Graph():
    def __init__(self, vertices):
        self.graph = [[0 for column in range(vertices)]\
                            for row in range(vertices)]
        self.V = vertices

    ''' Check if this vertex is an adjacent vertex
        of the previously added vertex and is not
        included in the path earlier '''
    def isSafe(self, v, pos, path):
        # Check if current vertex and last vertex
        # in path are adjacent
        if self.graph[ path[pos-1] ][v] == 0:
            return False

        # Check if current vertex not already in path
        for vertex in path:
            if vertex == v:
                return False

        return True

    # A recursive utility function to solve
    # hamiltonian cycle problem
    def hamCycleUtil(self, path, pos):

        # base case: if all vertices are
        # included in the path
        if pos == self.V:
            # Last vertex must be adjacent to the
            # first vertex in path to make a cyle
                return True

        # Try different vertices as a next candidate
        # in Hamiltonian Cycle. We don't try for 0 as
        # we included 0 as starting point in in hamCycle()
        for v in range(1,self.V):

            if self.isSafe(v, pos, path) == True:

                path[pos] = v

                if self.hamCycleUtil(path, pos+1) == True:
                    return True

                # Remove current vertex if it doesn't
                # lead to a solution
                path[pos] = -1

        return False

    def hamCycle(self):
        path = [-1] * self.V

        ''' Let us put vertex 0 as the first vertex
            in the path. If there is a Hamiltonian Cycle,
            then the path can be started from any point
            of the cycle as the graph is undirected '''
        path[0] = 0

        if self.hamCycleUtil(path,1) == False:
            print ("Solution does not exist\n")
            return False

        self.printSolution(path)
        return True

    def printSolution(self, path):
        print ("Solution Exists: Following is one Hamiltonian Cycle")
        for vertex in path:
            print (vertex,",")
        print (path[0], "\n")

# Driver Code
for i in range(4,20):
    g1 = Graph(i)
    g1.graph = createRandomMatrix(i)

    t = time()
    g1.hamCycle();
    t = time() - t
    log(i,t)
'''
g1.hamCycle();
g1 = Graph(5)
g1.graph = np.zeros((5,5))
 Print the solution
g1.hamCycle();

g2 = Graph(5)
g2.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
           [0, 1, 0, 0, 1,], [1, 1, 0, 0, 0],
           [0, 1, 1, 0, 0], ]

# Print the solution
g2.hamCycle();'''

# This code is contributed by Divyanshu Mehta
