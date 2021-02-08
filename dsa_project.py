'''
A Data Structure and Algorithm for the nearest point problem.

Data Structure: Binary Trees

Algorithm: Triangular Inequality

Git Hub Link: https://github.com/muh-nasiruit/dsa-project

Reference Material: https://ieeexplore.ieee.org/abstract/document/1703102/
'''

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
class Search:

    def __init__(self):
        self.root = None
        self.v = None
        self.LRADIUS = 0
        self.RRADIUS = 0
        self.pl = None
        self.pr = None
        self.v = None
        self.direction = None
        self.NL = []
        self.NR = []
        self.search_list = []
    
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
    
    def Placepoint1(self, val):
        self.v = self.__Placepoint(val, self.v)
        
    def __Placepoint1(self, val, v):

        if v == None:
            v = Node(val)
            self.pl = v
            self.pl.FULL = False
            # self.pl.ANCESTOR = w
            self.NL.append(self.pl)
        
        if v.FULL == False:
            self.pr = v
            self.FULL = True
            self.NR.append(self.pr)
        else:
            if abs(self.distance(val, self.pl.value)) < abs(self.distance(val, self.pr.value)):
                if len(self.NL) != 0:
                    self.LRADIUS = self.distance(self.NL(), self.pl.value)
                if abs(self.distance(val, self.pl.value)) > self.LRADIUS:
                    self.__Placepoint(val,v.LCHILD)
            else:
                if len(self.NR) != 0:
                    self.RRADIUS = self.distance(self.NR(), self.pr.value)
                if abs(self.distance(val, self.pr.value)) > self.RRADIUS:
                    self.__Placepoint(val, v.RCHILD)
                    
    
    def Placepoint(self, value):
        #wrapper function encapsulates the implementation technique
        self.root = self.__Placepoint(self.root, value)
        
    def __Placepoint(self, root, val):
        #if tree is empty
        if root is None:
            root = Node(val)
            
        else:
            if root.LCHILD == None:
                root.LCHILD = self.__Placepoint(root.LCHILD, val)
            
            else:
                if self.distance(root.value, val) > self.distance(root.value, root.LCHILD.value):
                    root.RCHILD = self.__Placepoint(root.LCHILD, val)
        
        return root
                
    def InOrder(self):
        return self.__InOrder(self.root)
    
    def __InOrder(self, root):
        if root:
            self.__InOrder(root.LCHILD)
            self.search_list.append(root.value)
            self.__InOrder(root.RCHILD)
    
    def NearestPoint(self, point):
        '''
        

        Parameters
        ----------
        point : tuple
            A point for which we search the nearest point.

        Returns
        -------
        tuple
            A point that is nearest to the point taken as input.

        '''
        self.InOrder()
        mini_list = []
        
        index = 0
        for i in self.search_list:
            x = mini_list.append(self.distance(i, point))
        
        mini_dist = min(mini_list)
        for j in self.search_list:
            if self.distance(j, point) == mini_dist:
                index +=1
                break
        
        return self.search_list[index]
                              
def Test():
    '''
    Driver Code to test this Project.

    Returns
    -------
    Nearest Point.

    '''
    obj = Search()
    obj.Placepoint((5,3))
    obj.Placepoint((2,8))
    obj.Placepoint((10,4))
    obj.Placepoint((11,2))
    obj.Placepoint((1,2))
    print(obj.NearestPoint((1,1)))

if __name__ == '__main__':
    Test()
