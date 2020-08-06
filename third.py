
class fly():
    def __init__(self,a,b):
        self.start=a
        self.stop=b
        self.present=a
        #list to store minpoints
        self.minp=[]
        self.minp.append(self.start)
        self.reached=False
        
rows,cols,height=(101,101,101)
memo=[[[True]*cols]*rows]*height

def gos(fly):
    if(fly.present==fly.stop):
        fly.reached=True
        return
    #checking whether the final point is in +ve or -ve direction and the further point is occupied or not
    #+ve direction of x
    if (fly.present[0] > fly.stop[0] and memo[fly.present[0]+1][fly.present[1]][fly.present[2]] ):
        memo[fly.present[0]][fly.present[1]][fly.present[2]] =True
        fly.present[0]+=1
    #-ve direction of x
    elif (fly.present[0] < fly.stop[0] and memo[fly.present[0]-1][fly.present[1]][fly.present[2]] ):
        memo[fly.present[0]][fly.present[1]][fly.present[2]] =True
        fly.present[0]-=1
    
    #+ve direction of y
    if (fly.present[1] > fly.stop[1] and memo[fly.present[0]][fly.present[1]+1][fly.present[2]] ):
        memo[fly.present[0]][fly.present[1]][fly.present[2]] =True
        fly.present[1]+=1
    #-ve direction of y
    elif (fly.present[1] < fly.stop[1] and memo[fly.present[0]][fly.present[1]-1][fly.present[2]] ):
        memo[fly.present[0]][fly.present[1]][fly.present[2]] =True
        fly.present[1]-=1
        
    #+ve direction of z
    if (fly.present[2] > fly.stop[2] and memo[fly.present[0]][fly.present[1]][fly.present[2]+1] ):
        memo[fly.present[0]][fly.present[1]][fly.present[2]] =True
        fly.present[2]+=1
    #-ve direction of z
    elif (fly.present[2] < fly.stop[2] and memo[fly.present[0]][fly.present[1]][fly.present[2]-1] ):
        memo[fly.present[0]][fly.present[1]][fly.present[2]] =True
        fly.present[2]-=1
    
    memo[fly.present[0]][fly.present[1]][fly.present[2]] =False
    minpoint=copy.copy(fly.present)
    fly.minp.append(minpoint)
        
def minPath(*args):
    flies=[]
    for inp in args:
        flie=fly(inp[0],inp[1])
        flies.append(flie)
    allreached= False
    while(not allreached):
        allreached=True
        for flie in flies:
            gos(flie)
            if not flie.reached:
                allreached=False
    return 0

a=[1,1,1]
b=[3,4,5]
c=[1,2,3]
d=[4,6,9]
points= [[a,b],[c,d]]
minPath(*points)
print("Hello world ")
