import numpy as np
Gset = []
def floodFill(G,visited,point):
    adj = []
    connected = []
    if point in visited:
        return
    visited.append(point)
    ###print("point",point,G)
    for edge in G:
        if edge[0] == point:
            adj.append(edge[1])
            connected.append(edge[1])
        if edge[1] == point:
            adj.append(edge[0])
            connected.append(edge[0])
    for vertex in adj:
        if vertex in visited:
            continue
        connected.extend(floodFill(G,visited,vertex))
    return connected

def findCutSet(e,T,edgeList,V,F,R):
    ###print("Number of Edges of Graph",3)
    G = []
    for edge in T:
        if edge != e:
            G.append(edge)
    ##print("Graph after cutting,",G)
    s2 = []
    s1 = [1]
    v = 1
    ###print("Number of Edges of Graph",len(G))
    s1.extend(floodFill(G,[],1))
    s1 = set(s1)
    ###print(s1)
    for edge in G:
        if edge[0] not in s1:
            s2.append(edge[0])
        if edge[1] not in s1:
            s2.append(edge[1])
    s2 = set(s2)
    #print("s1",s1)

    if(len(s2) == 0):
        for x in V:
            if x not in s1:
                s2.add(x)
                break
    #print("s2",s2)
    cutSet = []
    for edge in edgeList:
        cond = False
        if edge in G:
            continue
        if edge[0] in s1 and edge[1] in s2:
            cond = True
        if edge[1] in s1 and edge[0] in s2:
            cond = True
        if edge == e:
            cond = False
        if edge in F:
            cond = False
        if edge in R:
            cond = False
        if(cond):
            cutSet.append(edge)
    cutSet = set(cutSet)
    return cutSet




def ymw(F,R,G,edgeList,V,recCount):
    recCount += 1
    if(len(F) > len(V)):
        return
    #print("Graph is ",G)
    cutSets = {}
    k = len(F)
    if( k == 0 ):
        k = -1
    n = len(V)
    for count,edge in enumerate(G):
        cutSet = findCutSet(edge,G,edgeList,V,F,R)
        cutSets[edge] = cutSet
        #print("For edge",edge," The cut set is ",cutSet)
    #print(cutSets)
    #print("length of the Graph ",len(G))
    #print(k)
    #print(G)
    s = ""
    for i in range(30):
        s += "#"
    print(s)
    print("F",F)
    print("R",R)
    print("G",G)
    print(s+"\n")
    Gset.append(tuple(set(G)))
    for i in range(k+1,n-1):

        #print(i)
        e = G[i]
        #print("\nVertex ",e)
        #print(G)
        S = cutSets[e]
        if(len(cutSets[e]) == 0):
            #print("\nEmpty cutset")
            continue
        #print(S)
        #print("new F is ",G[k+1:i])
        Fi = list(F)
        Fi.extend(G[k+1:i])
        Fi = set(Fi)
        #print("F is ",Fi)
        Ri = []
        Ri.append(e)
        Ri.extend(R)
        Ri = set(Ri)
        #print("R is ", Ri)
        Gi = []
        for i in range(len(G)):
            Gi.append(G[i])
        Gi.remove(e)
        if(len(S) !=0):
            x = list(S)[0]
            #print("Adding x",x)
            Gi.append(x)
            cutSet = findCutSet(x,Gi,edgeList,V,Fi,Ri)
            cutSets[x] = cutSet
            ymw(Fi,Ri,Gi,edgeList,V,recCount)
def createInitialSpanningTree(edgeList,n,visited,source,G):
    visited[source] = 1
    G = []
    for edge in edgeList:
        if(edge[0] == source and visited[edge[1]] != 1):
            visited[edge[1]] = 1
            G.append(edge)
            G.extend(createInitialSpanningTree(edgeList,n,visited,edge[1],G))
        if(edge[1] == source and visited[edge[0]] != 1):
            visited[edge[0]] = 1
            G.append(edge)
            G.extend(createInitialSpanningTree(edgeList,n,visited,edge[0],G))
    return G

F = []
R = []
#edgeList = [(1,2),(1,3),(2,3),(2,4),(3,4),(3,5),(4,5),(4,6),(5,6)]
#G = [(1,2),(1,3),(2,4),(4,5),(4,6)]
print("Enter the number of Edges:")
numberOfEdges = int(input())
edgeList = []
print("Enter the Edges")
for i in range(numberOfEdges):
    a = input()
    x,y = a.split(" ")
    x = int(x)
    y = int(y)
    edge = (x,y)
    edgeList.append(edge)
#edgeList = [(1,2),(2,3),(3,4),(4,5),(5,2)]
print("edgeList",edgeList)
V = []
for x in edgeList:
    V.append(x[0])
    V.append(x[1])
V = set(V)
n = len(V)
visited = np.zeros((n+1))
G = []
G = createInitialSpanningTree(edgeList,n,visited,1,G)
print("Initial Spanning Tree",G)
recCount = 0
ymw(F,R,G,edgeList,V,recCount)
print("The spanning Trees are :")
for G in Gset:
    print(G)
