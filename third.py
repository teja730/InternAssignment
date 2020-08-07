
import copy
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
print("points -", points)

list =minPath(points)
for i in range(len(list)):
    print("Shortest Path for  ",i,"th set :")
    print(list[i])
