import heapq
import sys


class Node:
    def __init__(self,h_n,name):
        self.neigh = {}
        self.h_n = h_n
        self.name = name
    
    def add_neigh(self,neigh):
        self.neigh = neigh

    def __str__(self):
        return self.name

    def __lt__(self,other):
        return self.h_n < other.h_n

def PRINT(res):
    print()
    print("_____________________________ANSWER_________________________________")
    min_cost = sys.maxsize
    path=""
    for i in res:
        if i[0] < min_cost:
            min_cost = i[0]
            path = i[1]
    print("Cost: ", min_cost)
    print("Path: ", end="")
    for i in path:
        print(i, end= " ")
    

def fun():
    print(heap)
    i = 0
    while i<len(heap):
        j = i+1
        while j<len(heap) :
            if heap[i][1][-1] in heap[j][1] or heap[j][1][-1] in heap[i][1]:
                if heap[i][0]<heap[j][0] :
                    print("removed : ",heap[j][1])
                    heap.pop(j)
                    j-=1
                else:
                    print("removed : ",heap[i][1])
                    heap.pop(i)
                    i-=1
            j+=1
        i+=1


NodeA = Node(10,"A")
NodeB = Node(8,"B")
NodeC = Node(5,"C")
NodeD = Node(7,"D")
NodeE = Node(3,"E")
NodeF = Node(6,"F")
NodeG = Node(5,"G")
NodeH = Node(3,"H")
NodeI = Node(1,"I")
NodeJ = Node(0,"J")


NodeA.add_neigh({NodeF : 3,NodeB : 6})
NodeB.add_neigh({NodeA : 6,NodeD : 2, NodeC : 3})
NodeC.add_neigh({NodeB : 3,NodeD : 1, NodeE: 5})
NodeD.add_neigh({NodeB : 2,NodeC : 1, NodeE : 8})
NodeE.add_neigh({NodeC : 5,NodeD : 8, NodeI : 5, NodeJ:5})
NodeF.add_neigh({NodeA : 3,NodeG : 1, NodeH : 7})
NodeG.add_neigh({NodeF : 1, NodeI: 3})
NodeH.add_neigh({NodeF : 7, NodeI: 2})
NodeI.add_neigh({NodeE : 5, NodeG: 3, NodeH: 2, NodeJ:3})
NodeJ.add_neigh({NodeE: 5, NodeI: 3})


heap = []
heapq.heappush(heap,[10,[NodeA]])
ans = []
while len(heap)!=0:

    ele = heapq.heappop(heap)
    lastNode = ele[1][-1]
    path = ele[1].copy()

    if lastNode==NodeJ:
        ans.append(ele)
    
    ele[0] -= lastNode.h_n
    for node,cost in lastNode.neigh.items():
        if node in path:
            continue

        dummy = path.copy()
        dummy.append(node)
        heapq.heappush(heap,[ele[0]+node.h_n+cost,dummy])

    fun()
PRINT(ans)
