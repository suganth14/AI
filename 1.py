import heapq
import random

heap = []
heapq.heapify(heap)

arr = [ [7,2,4],
        [5,0,6],
        [8,3,1] ]

Final_ans = [
        [1,2,3],
        [4,5,6],
        [7,8,0]
]

def print_heap():
    for i in range(len(heap)):
        val = heap[i]
        #[val1,i-1,j,2,lvl+1,min_dit]
        print("LEVEL : ",val[4])
        print("manhattan : ",val[0])
        print("i j : ",val[1],val[2])
        print("cannot move to : ",val[3])
        print_arr(val[5])

def print_arr(dit):
    arr = [[0 for i in range(3)] for j in range(3)]
    print()
    for i in range(9):
        arr[dit[i][0]][dit[i][1]] = i
        
    for row in arr:
        print(row)
        
    print()
    
def printA():
    print()
    for row in arr:
        print(row)
    print()

def manhattan(dit2):
    ans = 0
    dit1 = {1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],0:[2,2]}
    print(dit2)
    for i in range(9):
        val1 = abs(dit1[i][0]-dit2[i][0])
        val2 = abs(dit1[i][1]-dit2[i][1])
        ans+=val1+val2
    return ans

def build_arr(dit):
    arr = [[0 for i in range(3)] for j in range(3)]
    for i in range(9):
        arr[dit[i][0]][dit[i][1]] = i
    return arr

def all_move(i,j,prev_move,lvl,dit):
    if(i-1>=0 and prev_move!=1):
        dit[arr[i][j]],dit[arr[i-1][j]] = dit[arr[i-1][j]],dit[arr[i][j]]
        Arr = build_arr(dit)
        val1 = manhattan(dit) + 1
        min_dit = dit.copy()
        build_arr(dit)
        #h_val,lvl,random_num,i,j,prev_move,dit,arr.copy()
        heapq.heappush(heap,[val1,lvl+1,random.randint(0,1000),i-1,j,2,min_dit,Arr])
        dit[arr[i][j]],dit[arr[i-1][j]] = dit[arr[i-1][j]],dit[arr[i][j]]
        
    if(i+1<=2 and prev_move!=2):
        dit[arr[i][j]],dit[arr[i+1][j]] = dit[arr[i+1][j]],dit[arr[i][j]]
        Arr = build_arr(dit)
        val2 = manhattan(dit)+ 1
        min_dit = dit.copy()
        heapq.heappush(heap,[val2,lvl+1,random.randint(0,1000),i+1,j,1,min_dit,Arr])
        dit[arr[i][j]],dit[arr[i+1][j]] = dit[arr[i+1][j]],dit[arr[i][j]]
    
    if(j-1>=0 and prev_move!=3):
        dit[arr[i][j]],dit[arr[i][j-1]] = dit[arr[i][j-1]],dit[arr[i][j]]
        Arr = build_arr(dit)
        val3 = manhattan(dit)+ 1
        min_dit = dit.copy()
        heapq.heappush(heap,[val3,lvl+1,random.randint(0,1000),i,j-1,4,min_dit,Arr])
        dit[arr[i][j]],dit[arr[i][j-1]] = dit[arr[i][j-1]],dit[arr[i][j]]
    
    if(j+1<=2 and prev_move!=4):
        dit[arr[i][j]],dit[arr[i][j+1]] = dit[arr[i][j+1]],dit[arr[i][j]]
        Arr = build_arr(dit)
        val4 = manhattan(dit)+ 1
        min_dit = dit.copy()
        heapq.heappush(heap,[val4,lvl+1,random.randint(0,1000),i,j+1,3,min_dit,Arr])
        dit[arr[i][j]],dit[arr[i][j+1]] = dit[arr[i][j+1]],dit[arr[i][j]]

dit = {}

for i in range(len(arr)):
    for j in range(len(arr[0])):
        dit[arr[i][j]] = [i,j]
        
i = 1
j = 1

prev_move = -1
print(dit)
h_val = manhattan(dit)
lvl = 1
random_num = random.randint(0,1000)

heapq.heappush(heap,[h_val,lvl,random_num,i,j,prev_move,dit,arr.copy()])
moves = 1000

while heap and moves>0:
    moves-=1

    ele = heapq.heappop(heap)
    i = ele[3]
    j = ele[4]
    arr = ele[-1]
    print("I J : ",i,j)
    printA()
    print("MAN : ",ele[0])
    print()
    prev_move = ele[5]
    lvl = ele[1]
    dit = ele[6]

    if(arr==Final_ans):
        print("FOUND SOLN!!!")
        break

    all_move(i,j,prev_move,lvl,dit.copy())
