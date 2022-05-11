import math
ipV = [[0.2,0.4]]
# ipV = [[-1,0]]

w = [[0.5,0.2],[0.1,0.4],[0.1,0.4],[0.6,0.9],[0.9,0.1]]
# w = [[0,-1],[-2/math.sqrt(5),1/math.sqrt(5)],[-1/math.sqrt(5),2/math.sqrt(5)]]
alpha = 0.2


for i in range(len(ipV)):
    c= []
    for j in range(len(w)):
        x = 0
        for k in range(len(ipV[i])):
            x += (ipV[i][k] - w[j][k])**2
        c.append(x)
    
    pos = c.index(min(c))

    
    for j in range(len(ipV[i])):
        w[pos][j] = w[pos][j] + alpha*(ipV[i][j] - w[pos][j])
        
    
print(w)