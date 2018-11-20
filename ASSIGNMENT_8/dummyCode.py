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
