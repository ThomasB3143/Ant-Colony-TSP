from node import *
import matplotlib.pyplot as plt
APC = 25 # constant - added pheromones coefficient
PDC = 0.9 # constant - pheromone decay constant
PPE = 0.9 # constant - pheromone priority exponent
DPE = -1.5 # constant - distance priority exponent
bestPath = []
bestDistance = -1
def setup(nodeList): # sets up initial matrices and carries out antRun() repeatedly
    # create pheromone and distance matrices
    global pheromoneMap
    pheromoneMap = [[1 for i in range(len(nodeList))] for j in range(len(nodeList))] #all points start with pheromones of 1
    global distanceMap
    distanceMap = [[0 for i in range(len(nodeList))] for j in range(len(nodeList))]
    # populate distanceMap
    for i in range(1,len(nodeList)):
        for j in range(0,i):
            distanceMap[j][i] = nodeList[i].distanceFrom(nodeList[j])
            distanceMap[i][j] = nodeList[i].distanceFrom(nodeList[j])

def antRun():
    global bestPath
    global bestDistance
    unvisited = list(range(1,len(distanceMap[0]))) # list of all univisited nodes (0 already removed)
    visited = [0] # will be appended in the order of nodes visited during the cycle
    currentNode = 0
    totalDistance = 0
    while unvisited: # while the unvisited list is not empty
        desireList = []
        for n in unvisited: # calculates desire for each unvisited node
            desireList.append(desireBetween(currentNode,n))
        chosenNode = choosePath(unvisited,desireList) # awesome probability function
        totalDistance += distanceMap[currentNode][chosenNode] # adds distance onto total for later pheromone addition
        currentNode = chosenNode # changes current node to desired node
        visited.append(chosenNode) # adds new node to visited
        unvisited.remove(chosenNode) # removes new node from unvisited
    totalDistance += distanceMap[visited[0]][visited[len(visited)-1]]
    if bestDistance == -1 or totalDistance < bestDistance:
        bestPath = visited
        bestDistance = totalDistance
    updatePheromones(visited, totalDistance)

def desireBetween(node1,node2): # inputs are the indexes of the nodes within the two matrices
    p = pheromoneMap[node1][node2]
    d = distanceMap[node1][node2]
    return (p**PPE)*(d**DPE)

def choosePath(choices,desires): # discrete probability function
    scaleFactor = sum(desires)
    for i in range(len(desires)):
        desires[i] /= scaleFactor
    return numpy.random.choice(a=choices,p=desires)

def updatePheromones(visited, totalDistance): # adds pheromones from the current ant and dissipates all pheromones by a factor
    for i in range(len(pheromoneMap)):
        for j in range(len(pheromoneMap)):
            pheromoneMap[i][j] *= (PDC)
    pheromoneToAdd = APC/totalDistance
    for i in range(len(visited)): # adding pheromones from the ant
        pheromoneMap[visited[i]][visited[(i+1)%len(visited)]] += pheromoneToAdd
        pheromoneMap[visited[(i+1)%len(visited)]][visited[i]] += pheromoneToAdd

'''node0 = Node(x=578,y=524)
node1 = Node(x=682,y=78)
node2 = Node(x=33,y=27)
node3 = Node(x=724,y=777)
node4 = Node(x=471,y=732)
node5 = Node(x=513,y=169)
node6 = Node(x=281,y=207)
node7 = Node(x=996,y=401)
node8 = Node(x=72,y=298)
node9 = Node(x=799,y=527)'''
#nodelist = [node0,node1,node2,node3,node4,node5,node6,node7,node8,node9]
nodelist = []
for i in range(70):
    nodelist.append(Node(numpy.random.randint(0,800),numpy.random.randint(0,800)))
setup(nodelist)
# optimal path is 0 4 3 9 7 1 5 2 8 6

for i in range(1000):
    antRun()
for i in range(len(pheromoneMap)):
        print(numpy.round(pheromoneMap[i],4))
print(bestPath)
print(bestDistance)

for i in range(0,len(bestPath)):
    plt.plot([nodelist[bestPath[i]].x,nodelist[bestPath[(i+1)%len(bestPath)]].x],[nodelist[bestPath[i]].y,nodelist[bestPath[(i+1)%len(bestPath)]].y],color=(1,0,0))

for i in range(0,len(nodelist)):
    plt.plot(nodelist[i].x,nodelist[i].y,"o")
    '''for j in range(i+1,len(nodelist)):
        strength = pheromoneMap[i][j]
        if strength > 0.001:
            plt.plot([nodelist[i].x,nodelist[j].x],[nodelist[i].y,nodelist[j].y],color=(1,0,0,strength))'''
plt.show()