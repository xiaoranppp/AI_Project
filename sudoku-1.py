import Queue
import copy
import numpy
var_char = ['A','B','C','D','E','F','G','H','I']
number=[0,1,2,3,4,5,6,7,8]
cubelist=[['A0','A1','A2','B1','B2','B0','C0','C1','C2'],['A3','A4','A5','B3','B4','B5','C3','C4','C5'],['A6','A7','A8','B6','B7','B8','C6','C7','C8'],
          ['D0','D1','D2','E1','E2','E0','F0','F1','F2'],['D3','D4','D5','E3','E4','E5','F3','F4','F5'],['D6','D7','D8','E6','E7','E8','F6','F7','F8'],
          ['G0','G1','G2','H1','H2','H0','I0','I1','I2'], ['G3','G4','G5','H3','H4','H5','I3','I4','I5'], ['G6','G7','G8','H6','H7','H8','I6','I7','I8']]
rlist= [ [0 for i in range(9)] for i in range(9)]
for i in range(9):
            for j in range(9):
                rlist[i][j]=(var_char[i]+str(number[j]))

clist= [ [0 for i in range(9)] for i in range(9)]
for i in range(9):
            for j in range(9):
                clist[j][i]=(var_char[i]+str(number[j]))

totallist=[]
for i in range(9):
            for j in range(9):
                totallist.append(var_char[i]+str(number[j]))




class CSP:

    def __init__(self,filename):
        self.value = [ [0 for i in range(9)] for i in range(9)]
        self.name = [ [0 for i in range(9)] for i in range(9)]
        self.domain=[]
        self.acset = []
        self.init(filename)
    
    def init(self,filename):
        tempvalue=[]
        for line in open(filename):
            temp=list(line.split(","))
            #temp=list(line.rstrip())
            tempvalue.append(temp)
        
        for i in range(9):
            for j in range(9):
                self.value[i][j]=tempvalue[i][j]
                self.name[i][j]=var_char[i]+str(number[j])
                if int(self.value[i][j])==0:
                    self.domain.append([1,2,3,4,5,6,7,8,9])
                else:
                    self.domain.append([int(self.value[i][j])])
        self.makeacset()
    def makeacset(self):
      
         for x in totallist:
             for y in totallist:
                 if((x[0] == y[0] and x[1] != y[1]) or (x[1] == y[1] and x[0] != y[0])):
                     if x!=y:
                        if [x,y] not in self.acset:
                            self.acset.append([x,y])
         
         for i in range(9):
             tempcube=cubelist[i]
             for x in tempcube:
                 for y in tempcube:
                     if x!=y:
                        if [x,y] not in self.acset:
                           self.acset.append([x,y])
     
             
         
    #########################################################################
    # set_cube_constraints() - setting variables for arc-consistency(cube).
    # Return: void
    #
    def get_neighbors(self,x):
        x_x=var_char.index(x[0])
        x_y=int(x[1])
        neighbor=[]
        for i in range(9):
            if self.name[x_x][i]!=x:
                neighbor.append(self.name[x_x][i])
            if self.name[i][x_y]!=x:
                neighbor.append(self.name[i][x_y])
        for i in range(9):
            if x in cubelist[i]:
                for j in range(9):
                    if cubelist[i][j] not in neighbor:
                       neighbor.append(cubelist[i][j])
        neighbor.remove(x)
        return(neighbor)
    def check(self,x,v):
        
        neighbors = self.get_neighbors(x)
        for n in neighbors:
            d = self.domain[totallist.index(n)]
            if(len(d) == 1 and v in d):
                return False
        return True

            
         
   
    #
def AC3(csp):
  
  queu = list(csp.acset)
  while queu:
    i, j = queu.pop()
    if revise(csp, i, j):
        for k in csp.get_neighbors(i) :
          if i != k:
            queu.append([k, i])
  
 


def revise(csp, i, j):
    revised = False
    A=csp.domain[totallist.index(i)]
    B=csp.domain[totallist.index(j)]
    if (len(B)==1 and len(A)!=1):
        if int(B[0]) in A:
           csp.domain[totallist.index(i)].remove(int(B[0]))
           revised = True
    return revised
def assignment(csp):
    assignment=[]
    print(len(csp.domain))
    for i in range(81):
        if len(csp.domain[i])==1:
            
            assignment.append(csp.domain[i][0])
        else:
            
            assignment.append(0)
    ass=[]
    for i in range(9):
        ass.append(assignment[i*9:(i+1)*9])
    return(ass)

def Forward(csp):
  changed = True
  while changed:
    AC3(csp)
    changed = False
    regions=rlist+clist+cubelist
    for r in regions: # for each region (row, column, box)
      domain = [1,2,3,4,5,6,7,8,9]
      [domain.remove(csp.domain[totallist.index(k)][0]) for k in r if len(csp.domain[totallist.index(k)]) == 1]
      for d in domain: # iterate over the values which haven't been assigned in that value
        if sum(csp.domain[totallist.index(k)].count(d) for k in r) == 1:
           for node in r:
               if d in csp.domain[totallist.index(node)]:
                  csp.domain[totallist.index(node)]=[d] 
                  changed = True
#coding=utf-8
import datetime
class solution(object):
    def __init__(self,board):
        self.b = board
        self.t = 0

    def check(self,x,y,value):
        for row_item in self.b[x]:
            if row_item == value:
                return False
        for row_all in self.b:
            if row_all[y] == value:
                return False
        row,col=x/3*3,y/3*3
        row3col3=self.b[row][col:col+3]+self.b[row+1][col:col+3]+self.b[row+2][col:col+3]
        for row3col3_item in row3col3:
            if row3col3_item == value:
                return False
        return True

    def get_next(self,x,y):
        for next_soulu in range(y+1,9):
            if self.b[x][next_soulu] == 0:
                return x,next_soulu
        for row_n in range(x+1,9):
            for col_n in range(0,9):
                if self.b[row_n][col_n] == 0:
                    return row_n,col_n
        return -1,-1  

    def try_it(self,x,y):
        if self.b[x][y] == 0:
            for i in range(1,10):
                self.t+=1
                if self.check(x,y,i):
                    self.b[x][y]=i 
                    next_x,next_y=self.get_next(x,y)
                    if next_x == -1: 
                        return True 
                    else:        
                        end=self.try_it(next_x,next_y)
                        if not end:
                            
                            self.b[x][y] = 0    
                        else:
                            return True

    def start(self):
        if self.b[0][0] == 0:
            self.try_it(0,0)
        else:
            x,y=self.get_next(0,0)
            self.try_it(x,y)
def check(csv):
    for i in csv.domain:
        if len(i)>1:
            return False
    return True
def write(csv):
        result=csv.domain
        result=[[0 for i in range(9)]for i in range (9)]
        kk=0
        for ii in range(9):
            for jj in range(9):
                result[ii][jj]=int(csv.domain[kk][0])
                kk=kk+1
        import csv
        with open('suoutput.txt','wb') as fb:
         writer = csv.writer(fb)
         writer.writerows(result)
         fb.close()
import csv
k=CSP('suinput.txt')
Forward(k)

t=check(k)
if t==True:
    write(k)
    print('easy sudoku')
else:
    ass=assignment(k)        
    s=solution(ass)
    s.start()
    with open('suoutput.txt','wb') as fb:
         writer = csv.writer(fb)
         writer.writerows(s.b)
