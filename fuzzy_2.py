A = [1,0.4,0.6,0.2]
B = [0,0.2,0.2,0.8]
C = [0.5,0.6,0.1,0.9]

def printArr(A):
    print()
    for i in A:
        print(i)
    print()

def cartesian(A,B):
    ans = [[0 for i in range(len(B))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B)):
            ans[i][j] = min(A[i],B[j])
    printArr(ans)
    return ans

def maxMin(A,B):
    ans = [[0 for i in range(len(B[0]))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            val = []
            for k in range(len(A[0])):
                val.append(min(A[i][k],B[k][j]))
            ans[i][j] = max(val)
    printArr(ans)
    
R = cartesian(A, B)
S = cartesian(A, C)
maxMin(R,S)
