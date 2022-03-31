start = (0,0)
cap1 = 4
cap2 = 3
end = (2,0)

poss = [[-cap1,0],[cap1,0],[0,cap2],[0,-cap2]]
q = [[start[0],start[1],[start]]]
notFound = True

def printQ(q):
    print()
    for ele in q:
        print(ele)
    print()

def fun(ele1,ele2,flag):
    if(flag==0):
        if(ele1>=cap1):
            ele1 = cap1
        if(ele1<=0):
            ele1 = 0
        if(ele2>=cap2):
            ele2=cap2
        if(ele2<=0):
            ele2 = 0
        return [ele1,ele2]
    else:
        var1 = 0
        if(ele1>=cap1):
            var1 = abs(cap1 - ele1)
            ele1 = cap1
            ele2 = var1
        if(ele2<=0):
            ele2 = 0
        if(ele2>=cap2):
            var1 = abs(cap2 - ele2)
            ele2=cap2
            ele1 = var1
        if(ele1<=0):
            ele1 = 0
        return [ele1,ele2]

visited = set()
visited.add((start[0],start[1]))

while(q and notFound):
    for i in range(len(q)):
        ele = q.pop(0)
        
        if(ele[0]==end[0] and ele[1]==end[1]):
            print("HHEHEHEHEHEA")
            print(ele[2])
            notFound = False
            break

        for dx,dy in poss:
            x,y = fun(ele[0]+dx,ele[1]+dy,0)
            if((x,y) not in visited):
                moves = ele[2].copy()
                moves.append((x,y))
                visited.add((x,y))
                q.append([x,y,moves])

        poss2 = [[ele[1],-ele[1]],[-ele[0],ele[0]]]
        for dx,dy in poss2:
            x,y = fun(ele[0]+dx,ele[1]+dy,1)
            if((x,y) not in visited):
                    moves = ele[2].copy()
                    moves.append((x,y))
                    visited.add((x,y))
                    q.append([x,y,moves])