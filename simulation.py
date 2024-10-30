from node import *
node1 = Node(x=10,y=10)
node2 = Node(x=20,y=20)
node3 = Node(x=40,y=20)
def begin(nodeList):

    pheremoneMap = [[] for i in range(len(nodeList))]*len(nodeList)
    distanceMap = [[] for i in range(len(nodeList))]*len(nodeList)

    # populate distanceMap
    for i in range(0,len(nodeList)-1):
        print("i = ",i)
        for j in range(i+1,len(nodeList)-1):
            print("j = ",j)
            distanceMap[i][j] = nodeList[i].distanceFrom(nodeList[j])
            distanceMap[j][i] = nodeList[i].distanceFrom(nodeList[j])
    print(distanceMap)
begin([node1,node2,node3])