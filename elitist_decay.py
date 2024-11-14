from node import *
import matplotlib.pyplot as plt
APC = 25 # constant - added pheromones coefficient
PDC = 0.9 # constant - pheromone decay constant
PFC = 0.8 # constant - pheromone fall-off coefficient (the factor change for pheromones added to the strongest trail ) 
PPE = 0.9 # constant - pheromone priority exponent
DPE = -2 # constant - distance priority exponent
APB = 20 # ants per batch
bestPath = []
bestDistance = -1
batchBest = APB
antCount = 0
bestBatch = 0
newBestCount = 0
initialDistance = 0 # distance of nearest neighbour solution
distanceImprovement = 0  # improvement from nearest neighbour solution
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
def fullRun():
    global bestPath
    global bestDistance
    global batchBest
    global antCount
    global bestBatch
    global newBestCount
    global initialDistance
    global distanceImprovement
    bestPath = []
    bestDistance = -1
    batchBest = APB
    antCount = 0
    bestBatch = 0
    newBestCount = 0
    initialDistance = 0 
    distanceImprovement = 0
    for i in range(1000//APB):
        antRun(APB)
    '''for i in range(len(pheromoneMap)):
        print(numpy.round(pheromoneMap[i],4))'''
    print("Best batch was number: ",bestBatch)
    print("Total number of batches was: ", 1000//APB)
    print("Total times a better path was found is: ",newBestCount)
    print("Best distance - initial distance = ", bestDistance, " - ", initialDistance, " = ", bestDistance-initialDistance)
    print("")
def antRun(n): # this is now recursive, n is the ID of the ant in the batch and the number of ants left to do
    global bestPath
    global bestDistance
    global batchBest
    global bestBatch
    global antCount
    global newBestCount
    global initialDistance
    unvisited = list(range(1,len(distanceMap[0]))) # list of all univisited nodes (0 already removed)
    visited = [0] # will be appended in the order of nodes visited during the cycle
    currentNode = 0
    totalDistance = 0
    antCount += 1
    while unvisited: # while the unvisited list is not empty
        desireList = []
        for node in unvisited: # calculates desire for each unvisited node
            desireList.append(desireBetween(currentNode,node))
        chosenNode = choosePath(unvisited,desireList) # awesome probability function
        totalDistance += distanceMap[currentNode][chosenNode] # adds distance onto total for later pheromone addition
        currentNode = chosenNode # changes current node to desired node
        visited.append(chosenNode) # adds new node to visited
        unvisited.remove(chosenNode) # removes new node from unvisited
    totalDistance += distanceMap[visited[0]][visited[len(visited)-1]]
    if antCount == 1: # first ant
        initialDistance = totalDistance
    if bestDistance == -1 or totalDistance < bestDistance:
        bestPath = visited
        bestDistance = totalDistance
        batchBest = n
        bestBatch = antCount//APB
        newBestCount += 1
    if n > 0:
        antRun(n-1)
    best = False
    if batchBest == n:
        best = True
    updatePheromones(visited, totalDistance, best)

def desireBetween(node1,node2): # inputs are the indexes of the nodes within the two matrices
    p = pheromoneMap[node1][node2]
    d = distanceMap[node1][node2]
    return (p**PPE)*(d**DPE)

def choosePath(choices,desires): # discrete probability function
    scaleFactor = sum(desires)
    for i in range(len(desires)):
        desires[i] /= scaleFactor
    return numpy.random.choice(a=choices,p=desires)

def updatePheromones(visited, totalDistance, best): # adds pheromones from the current ant and dissipates all pheromones by a factor
    for i in range(len(pheromoneMap)):
        for j in range(len(pheromoneMap)):
            pheromoneMap[i][j] *= (PDC)
    pheromoneToAdd = APC/totalDistance
    maxStrength = numpy.amax(pheromoneMap)
    if best:
        pheromoneToAdd *= 2
    for i in range(len(visited)): # adding pheromones from the ant
        pheromoneMap[visited[i]][visited[(i+1)%len(visited)]] += pheromoneToAdd * PFC**(pheromoneMap[visited[i]][visited[(i+1)%len(visited)]] / maxStrength)
        pheromoneMap[visited[(i+1)%len(visited)]][visited[i]] += pheromoneToAdd * PFC**(pheromoneMap[(i+1)%len(visited)][visited[i]] / maxStrength)