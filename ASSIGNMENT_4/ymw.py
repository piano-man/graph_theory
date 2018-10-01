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

def findCutSet(e,T,edgeList,V):
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
        if(cond):
            cutSet.append(edge)
    cutSet = set(cutSet)
    return cutSet




def ymw(F,R,G,edgeList,V):
    ##print("Graph is ",G)
    cutSets = {}
    k = len(F)
    n = len(V)
    for count,edge in enumerate(G):
        cutSet = findCutSet(edge,G,edgeList,V)
        cutSets[edge] = cutSet
        #print("For edge",edge," The cut set is ",cutSet)
    #print(cutSets)
    #print("length of the Graph ",len(G))
    #print(k)
    for i in range(k+1,n-1):
        #print(i)
        e = G[i]
        S = cutSets[e]
        #print(S)
        for j in range(k+1,i-1):
            F.union(set(G[j]))
            print(set(G[j]))
        print("F is ",F)
        R.union(set(e))
        print("R is ", R)
        G.remove(e)
        for x in S:
            #print("Adding x",x)
            G.append(x)
            cutSet = findCutSet(x,G,edgeList,V)
            cutSets[x] = cutSet
            break

F = set()
R = set()
edgeList = [(1,2),(1,3),(2,3),(2,4),(3,4),(3,5),(4,5),(4,6),(5,6)]
G = [(1,2),(1,3),(2,4),(4,5),(4,6)]
V = []
for x in G:
    V.append(x[0])
    V.append(x[1])
V = set(V)
ymw(F,R,G,edgeList,V)
