import math
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distanceFrom(self, n2):
        return math.sqrt((self.x - n2.x)^2 + (self.y - n2.y)^2)