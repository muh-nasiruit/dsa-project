'OUR PROJECT'

from math import *

class Node:
    def __init__(self, p):
        self.value = p
        self.LCHILD = None
        self.RCHILD = None
        self.LRADIUS = 0
        self.RRADIUS = 0
        self.FULL = False
    
    def TempStorage(self, direction):
        direction = 
        
#root.left = LCHILD
#root.right = RCHILD
#NODEPOINTER = self.root
class BST:
    def __init__(self):
        self.root = None
        self.direction = None
        
    def distance(self, p1, p2):
        dist = sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
        res = float('{:.2}'.format(dist))
        return res
        
    def Decision(self, direction):
        self.direction = direction
    
    def Insert(self, value):
        #wrapper function encapsulates the implementation technique
        self.root = self.__Insert(self.root, value)
        
    def __Insert(self, root, value):
        #this is where the big boy stuff will happen
        if root is None:
            root = Node(value)
            
        else:
            #instead of value it will be self.distance(value, root.right) i guess
            if self.distance(value > root.value:
                root.pr = self.__Insert(root.pl, value)
            
            else:
                root.pl = self.__Insert(root.pl, value)
        
        return root

    
    

'''
Calculation for the distance between two points
'''  
# p1 = (2, 1)
# p2 = (5, 3)

# dist = sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
# res = float('{:.2}'.format(dist))
# print(res)
    
