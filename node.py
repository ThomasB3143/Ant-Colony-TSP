import math
import numpy
l = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(l)):
    for j in range(len(l)):
        l[i][j] += 1
print(l)
l2 = [1,2]
p1 = [0.05,0.5]
factor = sum(p1)
for i in range(len(p1)):
    p1[i] /= factor
print(p1)
print(numpy.random.choice(a=l2, p=p1))

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distanceFrom(self, n2):
        return math.sqrt((self.x - n2.x)**2 + (self.y - n2.y)**2)