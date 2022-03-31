def isValid(ele):
    miss = 3 - ele[0]
    can = 3 - ele[1]
    if((ele[0]>0 and ele[1]>ele[0]) or (miss>0 and can>miss)):
        return False
    return True


visited = []

q = [[3,3,'L']]
notFound = True


while(q and notFound):
    print()
    for i in range(len(q)):
        ele = q.pop(0)
        visited.append(ele)
        print(ele)

        if(ele==[0,0,'R']):
            print("Found soln")
            notFound = False
            break

        if(ele[-1]=='L'):
            if(ele[0]>=2):
                arr = ele.copy()
                arr[0]-=2
                arr[2] = 'R'
                if isValid(arr) and arr not in visited and arr not in q:
                    q.append(arr.copy())

            if(ele[1]>=2):
                arr = ele.copy()
                arr[1]-=2
                arr[2] = 'R'
                if isValid(arr) and arr not in visited and arr not in q:
                    q.append(arr.copy())

            if(ele[0]>=1 and ele[1]>=1):
                arr = ele.copy()
                arr[0]-=1
                arr[1]-=1
                arr[2] = 'R'
                if isValid(arr) and arr not in visited and arr not in q:
                    q.append(arr.copy())

        else:
            if(ele[0]<=2):
                arr = ele.copy()
                arr[0]+=1
                arr[2] = 'L'
                if isValid(arr) and arr not in visited and arr not in q:
                    q.append(arr.copy())

            if(ele[1]<=2):
                arr = ele.copy()
                arr[1]+=1
                arr[2] = 'L'
                if isValid(arr) and arr not in visited and arr not in q:
                    q.append(arr.copy())
            
            if(ele[0]<=2 and ele[1]<=2 and arr not in q):
                arr = ele.copy()
                arr[0]+=1
                arr[1]+=1
                arr[2] = 'L'
                if isValid(arr) and arr not in visited:
                    q.append(arr.copy())