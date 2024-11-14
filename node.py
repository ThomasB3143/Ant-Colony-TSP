import math
import numpy
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distanceFrom(self, n2):
        return math.sqrt((self.x - n2.x)**2 + (self.y - n2.y)**2)
    def generateNodeList(n): # n is the number of nodes
        nodelist = []
        for i in range(60):
            nodelist.append(Node(numpy.random.randint(0,800),numpy.random.randint(0,800)))
        return nodelist