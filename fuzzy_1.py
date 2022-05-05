A = {
     2:1,
     3:0.4,
     1:0.6,
     4:0.2
     }

B = {
     2:0,
     3:0.2,
     1:0.2,
     4:0.8
     }

def union(A,B):
    ans = {}
    for key,val in A.items():
        ans[key] = max(A[key],B[key])
    return ans

def intersection(A,B):
    ans = {}
    for key,val in A.items():
        ans[key] = min(A[key],B[key])
    return ans

def complement(dit):
    ans = {}
    for key,val in dit.items():
        ans[key] = 1-val
    return ans

def PRINT(dit):
    string = "{ "
    for k,val in dit.items():
        string+=str(val)+"/"+str(k) + " + "
    string = string[:-2]
    string+="}"
    print(string)
    return string
    
def verifyDemorgan(A,B):
    LHS = complement(intersection(A,B))
    RHS = union(complement(A),complement(B))
    if LHS==RHS:
        print("Verified")
    else:
        print("Wrong")

PRINT(union(A,B))
PRINT(intersection(A,B))
PRINT(complement(A))
verifyDemorgan(A, B)