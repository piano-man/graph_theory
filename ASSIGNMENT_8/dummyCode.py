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
		if(idList[neighbor] > idList[vertex] and joined[neighbor] != True):
			MIS.append(v)
