def updateW(index,inpIndex):
    for i in range(len(W)):
        W[i][index] = W[i][index] + alpha*(I[inpIndex][i]-W[i][index])

W = [
    [0.5,0.1,0.1,0.6,0.9],
    [0.2,0.4,0.4,0.9,0.1]
    ]

I = [[0.2,0.4]]
alpha = 0.2

for i in range(len(I)):
    arr = []
    for j in range(len(W[0])):
        val = 0
        for k in range(len(W)):
            val+=I[i][k]*W[k][j]
        arr.append(val)
    updateW(arr.index(min(arr)),i)
print(W)
