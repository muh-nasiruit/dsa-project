'OUR PROJECT'

from math import *

class Node:
    def __init__(self, p):
        self.value = p
        self.LCHILD = None
        self.RCHILD = None
        self.FULL = False
        self.ANCESTOR = None
    
    def TempStorage(self, direction):
        direction = None
        
#root.left = LCHILD
#root.right = RCHILD
#NODEPOINTER = self.root
class BST:

    def __init__(self):
        self.LRADIUS = 0
        self.RRADIUS = 0
        self.pl = None
        self.pr = None
        self.v = None
        self.direction = None
        self.NL = []
        self.NR = []
    
    def NL(self):
        if len(self.NL) != 0:
            x = max(self.NL,key=lambda item:item[0])[0]
            y = max(self.NL,key=lambda item:item[1])[1]
            t = (x, y)
        return t
    
    def RL(self):
        if len(self.NR) != 0:
            x = max(self.NR,key=lambda item:item[0])[0]
            y = max(self.NR,key=lambda item:item[1])[1]
            t = (x, y)
        return t
        
    def distance(self, p1, p2):
        '''
        

        Parameters
        ----------
        p1 : int
            point 1 (x1,y1)
        p2 : int
            point 2 (x2, y2)

        Returns
        -------
        res : float
            distance between point1 and point2

        '''
        dist = sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
        res = float('{:.2}'.format(dist))
        return res
        
    def Decision(self, direction):
        self.direction = direction #WENT LEFT/WENT RIGHT
    
    def Placepoint(self, val, v, w):
        if v == None:
            v = Node(val)
            self.pl = v
            self.pl.FULL = False
            self.pl.ANCESTOR = w
            self.NL.append(self.pl)
        
        if v.FULL == False:
            self.pr = val
            self.FULL = True
            self.NR.append(self.pr)
        else:
            if abs(self.distance(val, self.pl.value)) < abs(self.distance(val, self.pr.value)):
                if len(self.NL) != 0:
                    self.LRADIUS = self.distance(self.NL(), self.pl.value)
                if abs(self.distance(val, self.pl.value)) > self.LRADIUS:
                    self.Placepoint(val, v.LCHILD, v)
            else:
                if len(self.NR) != 0:
                    self.RRADIUS = self.distance(self.NR(), self.pr.value)
                if abs(self.distance(val, self.pr.value)) > self.RRADIUS:
                    self.Placepoint(val, v.RCHILD, v)
                
                    
                    
                              
            

    
    

'''
Calculation for the distance between two points
'''  
# p1 = (2, 1)
# p2 = (5, 3)

# dist = sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
# res = float('{:.2}'.format(dist))
# print(res)
    
