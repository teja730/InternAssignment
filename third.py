
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import copy
import random
class fly():
    
    
    def __init__(self,a,b):
        self.start=a
        self.stop=b
        self.present=copy.copy(a)
        #list to store minpoints
        self.minp=[]
        self.minp.append(a)
        self.reached=False
        


def gos(fly):
    if(fly.present==fly.stop):
        fly.reached=True
        return
    #checking whether the final point is in +ve or -ve direction and the further point is occupied or not
    #+ve direction of x
    #print ("present ",fly.present)
    #print ("stop ",fly.stop)
    #print ("memo ",memo[2][1][1] )
    if (fly.present[0] < fly.stop[0] and memo[fly.present[0]+1][fly.present[1]][fly.present[2]] ):
        #print (memo[fly.present[0]+1][fly.present[1]][fly.present[2]])
        memo[fly.present[0]][fly.present[1]][fly.present[2]] =True
        fly.present[0]+=1
    #-ve direction of x
    elif (fly.present[0] > fly.stop[0] and memo[fly.present[0]-1][fly.present[1]][fly.present[2]] ):
        memo[fly.present[0]][fly.present[1]][fly.present[2]] =True
        fly.present[0]-=1
    
    #+ve direction of y
    elif (fly.present[1] < fly.stop[1] and memo[fly.present[0]][fly.present[1]+1][fly.present[2]] ):
        memo[fly.present[0]][fly.present[1]][fly.present[2]] =True
        fly.present[1]+=1
    #-ve direction of y
    elif (fly.present[1] > fly.stop[1] and memo[fly.present[0]][fly.present[1]-1][fly.present[2]] ):
        memo[fly.present[0]][fly.present[1]][fly.present[2]] =True
        fly.present[1]-=1
        
    #+ve direction of z
    elif (fly.present[2] < fly.stop[2] and memo[fly.present[0]][fly.present[1]][fly.present[2]+1] ):
        memo[fly.present[0]][fly.present[1]][fly.present[2]] =True
        fly.present[2]+=1
    #-ve direction of z
    elif (fly.present[2] > fly.stop[2] and memo[fly.present[0]][fly.present[1]][fly.present[2]-1] ):
        memo[fly.present[0]][fly.present[1]][fly.present[2]] =True
        fly.present[2]-=1
    
    #print (fly.present)
    memo[fly.present[0]][fly.present[1]][fly.present[2]] =False
    minpoint=copy.copy(fly.present)
    fly.minp.append(minpoint)
        
def minPath(args):
    minpathlist=[]
    flies=[]
    for inp in args:
        flie=fly(inp[0],inp[1])
        #print("inp[0] -",inp[0])
        memo[inp[0][0]][inp[0][1]][inp[0][2]] =False
        flies.append(flie)
    #print (memo)
    allreached= False
    while(not allreached):
        allreached=True
        for flie in flies:
            gos(flie)
            if not flie.reached:
                allreached=False
    for flie in flies:
        minpathlist.append(flie.minp)
    return minpathlist
    
    
rows,cols,height=(101,101,101)
grid=[[[random.randint(0,100) for i in range(cols)] for j in range(rows)] for k in range(height)]
memo=[[[True for i in range(cols)] for j in range(rows)] for k in range(height)]
points=[]
sets=int(input("Enter the number of sets:"))

for i in range(sets):
    ax=int(input("X-coordinate of start point of "+str(i+1)+"th set: "))
    ay=int(input("Y-coordinate of start point of "+str(i+1)+"th set: "))
    az=int(input("Z-coordinate of start point of "+str(i+1)+"th set: "))
    startpoint=[ax,ay,az]
    bx=int(input("X-coordinate of end point of "+str(i+1)+"th set: "))
    by=int(input("Y-coordinate of end point of "+str(i+1)+"th set: "))
    bz=int(input("Z-coordinate of end point of "+str(i+1)+"th set: "))
    endpoint=[bx,by,bz]
    points.append([startpoint,endpoint])
#a=[1,1,1]
#b=[3,4,5]
#c=[1,2,3]
#d=[4,6,9]
#points1= [[a,b],[c,d]]
#print("points1 -", points1)
#print("points -", points)
list =minPath(points)

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')
colors = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(sets)]
for i in range(len(list)):
    X=[]
    Y=[]
    Z=[]
    print("Shortest Path for  ",i,"th set :")
    print(list[i])
    for j in range(len(list[i])):
        X.append(list[i][j][0])
        Y.append(list[i][j][1])
        Z.append(list[i][j][2])
        
    ax.plot(X, Y, Z,color=colors[i])
    

ax.set_title('wireframe')
plt.show()
