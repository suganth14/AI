arr = [
      [1,2,3],
      [0,4,6],
      [7,5,8]
      ]

# arr = [
#        [7,2,4],
#        [5,0,6],
#        [8,3,1]
#       ]

def print_arr(dit):
    arr = [[0 for i in range(3)] for j in range(3)]
    print()
    for i in range(9):
        arr[dit[i][0]][dit[i][1]] = i
        
    for row in arr:
        print(row)
        
    print()
    
def misplaced(dit2):
    ans=0
    dit1 = {1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],0:[2,2]}
    for k,val in dit2.items():
        if(val!=dit1[k]):
            ans+=1
    return ans

def manhattan(dit2):
    ans = 0
    dit1 = {1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],0:[2,2]}
    for i in range(9):
        val1 = abs(dit1[i][0]-dit2[i][0])
        val2 = abs(dit1[i][1]-dit2[i][1])
        ans+=val1+val2
    return ans
        
def all_move(i,j,prev_h):
    min_dit = False
    move = None
    if(i-1>=0):
        dit[arr[i][j]],dit[arr[i-1][j]] = dit[arr[i-1][j]],dit[arr[i][j]]
        val1 = manhattan(dit) + misplaced(dit)
        if prev_h>val1:
            prev_h = val1
            min_dit = dit.copy()
            move = 1
        dit[arr[i][j]],dit[arr[i-1][j]] = dit[arr[i-1][j]],dit[arr[i][j]]
        
    if(i+1<=2):
        dit[arr[i][j]],dit[arr[i+1][j]] = dit[arr[i+1][j]],dit[arr[i][j]]
        val2 = manhattan(dit)+ misplaced(dit)
        if prev_h>val2:
            prev_h = val2
            min_dit = dit.copy()
            move = 2
        dit[arr[i][j]],dit[arr[i+1][j]] = dit[arr[i+1][j]],dit[arr[i][j]]
    
    if(j-1>=0):
        dit[arr[i][j]],dit[arr[i][j-1]] = dit[arr[i][j-1]],dit[arr[i][j]]
        val3 = manhattan(dit)+ misplaced(dit)
        if prev_h>val3:
            prev_h = val3
            min_dit = dit.copy()
            move = 3
        dit[arr[i][j]],dit[arr[i][j-1]] = dit[arr[i][j-1]],dit[arr[i][j]]
    
    if(j+1<=2):
        dit[arr[i][j]],dit[arr[i][j+1]] = dit[arr[i][j+1]],dit[arr[i][j]]
        val4 = manhattan(dit)+ misplaced(dit)
        if prev_h>val4:
            prev_h = val4
            min_dit = dit.copy()
            move = 4
        dit[arr[i][j]],dit[arr[i][j+1]] = dit[arr[i][j+1]],dit[arr[i][j]]
    
    if min_dit:
        return [min_dit,prev_h,move]
    return False

dit = {}

for i in range(len(arr)):
    for j in range(len(arr[0])):
        dit[arr[i][j]] = [i,j]
        
pos = [1,0]
h_val = manhattan(dit)+misplaced(dit)

while True:
    i,j = pos[0],pos[1]
    if h_val == 0:
        print("Found Soln")
        break

    flag = False
    flag = all_move(pos[0], pos[1], h_val)
    
    if(flag==False):
        print("sad")
        break
    
    dit = flag[0]
    h_val = flag[1]
    move = flag[2]
    if(move == 1):
        arr[i][j],arr[i-1][j] = arr[i-1][j],arr[i][j]
        pos[0]-=1
    elif(move==2):
        arr[i][j],arr[i+1][j] = arr[i+1][j],arr[i][j]
        pos[0]+=1
    elif(move==3):
        arr[i][j],arr[i][j-1] = arr[i][j-1],arr[i][j]
        pos[1]-=1
    elif(move==4):
        arr[i][j],arr[i][j+1] = arr[i][j+1],arr[i][j]
        pos[1]+=1
        
    print_arr(dit)
    print(pos)