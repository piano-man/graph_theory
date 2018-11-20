graph = edgeList


MIS = []
for v in vertices:
  neighbors = []
  for edge in edgeList:
    if v == edge[0]:
      neighbors.append(edge[1])
    if v == edge[1]:
      neighbors.append(edge[2])
    for neighbor in neighbors:
        nonRepeatCond = (idList[neighbor] > idList[vertex])
        isNotJoined = ( joined[neighbor] != True)
        if(nonRepeatCond and isNotJoined):
           MIS.append(v)


def fastMIS(vertices,phases):
    MST
    for phase in phases:
	#randomising the vertices first
	for v in vertices:
	    rand[v] = float(random.randInt(0,100))/100.
	#selecting one v from the vertices
	for v2 in vertices:
	    isLessThanAll = True
	    for v2 in vertices:
		if(rand[v2] < rand[v1]):
		    isLessThanAll = False
		    break
	    if(isLessThanAll):
		MST.append(v)
		#terminating v by removing all the edges of v
		vertices.remove(v)
		removableList = []
		for edge in edgeList:
		    if(edge[0] == v or edge[1] == v):
		    removableList.append(edge)
		for edge in removableList:
		    edgeList.remove(edge)
    return MST

			
			
	
