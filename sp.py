inst = [["mi",11,13],["mi",9,12],["mi",8.5,18],["mi",12,8],["mi",13,18],["a",18,5],["a",20,7.5]
     ,["a",16.5,6],["a",19,6.5],["a",12,9]]

w = [-0.3,1]

f = True
alpha = 0.01
loopcondn = 0
while(f):
    for i in range(len(inst)):
        
        if(loopcondn>=len(inst)-1):
            f = False
            break
        
        x = 0
        for j in range(len(w)):
            x += inst[i][j+1]*w[j]

        if x > 0:
            if inst[i][0] != "mi" :
                for j in range(len(w)):
                    w[j] = w[j] + alpha*(-1)*inst[i][j+1]
                    loopcondn = 0
                break
            else:
                loopcondn+=1
                continue
        if x < 0 :
            if inst[i][0] != "a":
                for j in range(len(w)):
                    w[j] = w[j] + alpha*(1)*inst[i][j+1]
                    loopcondn = 0
                break
            else:
                loopcondn+=1
                continue

print("Updated W : ",w)
