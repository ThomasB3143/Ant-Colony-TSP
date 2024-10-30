from node import *
apc = 20 # constant - added pheromones coefficient
pdc = 0.2 # constant - pheromone decay constant
ppe = 1.5 # constant - pheromone priority exponent
dpe = 1.5 # constant - distance priority exponent
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
    #print matrix
    for i in range(len(nodeList)):
        print(distanceMap[i])

def antRun():
    print("BEGGINING ANT RUN")
    unvisited = list(range(1,len(distanceMap[0]))) # list of all univisited nodes (0 already removed)
    visited = [0] # will be appended in the order of nodes visited during the cycle
    print("univisted: ",unvisited)
    currentNode = 0
    totalDistance = 0
    while unvisited: # while the unvisited list is not empty
        desireList = []
        print("currentNode: ",currentNode)
        print("unvisited in loop: ",unvisited)
        print("visited in loop: ",visited)
        for n in unvisited: # calculates desire for each unvisited node
            desireList.append(desireBetween(currentNode,n))
        print("desireList in loop: ",desireList)
        chosenNode = desireList.index(max(desireList)) # replace with probability function
        totalDistance += distanceMap[currentNode][chosenNode] # adds distance onto total for later pheromone addition
        currentNode = unvisited[chosenNode] # changes current node to desired node
        visited.append(unvisited[chosenNode]) # adds new node to visited
        del unvisited[chosenNode] # removes new node from unvisited
    print(visited)
    print(totalDistance)
    # path is now made, write the pheromone secretion code here
    updatePheromones(visited, totalDistance)
    for i in range(len(pheromoneMap)):
        print(pheromoneMap[i])



def desireBetween(node1,node2): # inputs are the indexes of the nodes within the two matrices
    p = pheromoneMap[node1][node2]
    d = distanceMap[node1][node2]
    return p/d
def updatePheromones(visited, totalDistance): # adds pheromones from the current ant and dissipates all pheromones by a factor
    pheromoneToAdd = 5
    for i in range(len(visited)):
        pheromoneMap[visited[i]][visited[(i+1)%len(visited)]] += pheromoneToAdd
        pheromoneMap[visited[(i+1)%len(visited)]][visited[i]] += pheromoneToAdd

node0 = Node(x=10,y=10)
node1 = Node(x=20,y=20)
node2 = Node(x=40,y=20)
node3 = Node(x=15,y=5)
node4 = Node(x=15,y=10)
node5 = Node(x=25,y=10)
setup([node0,node1,node2,node3,node4,node5])
antRun()