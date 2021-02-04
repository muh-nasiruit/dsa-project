'OUR PROJECT'

from math import *

class Node:
    def __init__(self, p):
        self.value = p
        self.pl = None
        self.pr = None
#root.left = pl
#root.right = pr
class BST:
    def __init__(self):
        self.root = None
        
    def distance(self, p1, p2):
        dist = sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
        res = float('{:.2}'.format(dist))
        return res
        
        
    def Insert(self, value):
        #wrapper function encapsulates the implementation technique
        self.root = self.__Insert(self.root, value)
        
    def __Insert(self, root, value):
        #this is where the big boy stuff will happen
        if root is None:
            root = Node(value)
            
        else:
            #instead of value it will be self.distance(value, root.right) i guess
            if value > root.value:
                root.right = self.__Insert(root.right, value)
            
            else:
                root.left = self.__Insert(root.left, value)
        
        return root

    
    

'''
Calculation for the distance between two points
'''  
# p1 = (2, 1)
# p2 = (5, 3)

# dist = sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
# res = float('{:.2}'.format(dist))
# print(res)
    
