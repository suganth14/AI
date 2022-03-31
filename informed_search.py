import networkx as nx
import matplotlib.pyplot as plt

adj_list = {
        5 : [3],
        3 : [2,4,5],
        7 : [8],
        2 : [3],
        4 : [8,3],
        8 : [4,7]
        }

def bfs(i,j):
    ans = []
    q = []
    q.append([i])
    while(q):
        ele = q.pop(0)
        node = ele[-1]
        if(node==j):
            ans.append(ele)
        for x in adj_list[node]:
            if(x not in ele):
                new_path = list(ele)
                new_path.append(x)
                q.append(new_path)
    return ans    

def dfs(i,j):
    ans = []
    q = []
    q.append([i])
    while(q):
        ele = q.pop(-1)
        node = ele[-1]
        if(node==j):
            ans.append(ele)
        for x in adj_list[node]:
            if(x not in ele):
                new_path = list(ele)
                new_path.append(x)
                q.append(new_path)
    return ans


def depth_limited(i,j,val,stack):
    if(val==-1):
        return
    
    if(stack[-1]==j):
        depth_ans.append(stack)
        return
    
    ele = stack[-1]
    for x in adj_list[ele]:
        if(x not in stack):
            depth_limited(i,j,val-1,stack+[x])
    
def iterative_deep(i,j,val,stack):
    if(val==-1):
        return
    
    if(stack[-1]==j):
        iter_ans.append(stack)
        return
    
    ele = stack[-1]
    for x in adj_list[ele]:
        if(x not in stack):
            iterative_deep(i,j,val-1,stack+[x])
            
temp = bfs(5,8)
depth_ans = []
depth_limited(5,2,5,[5])
print(depth_ans)

i=0
iter_ans = []
while(len(iter_ans)==0):
    iterative_deep(5,7,i,[5])
    i+=1
print(iter_ans,i-1)

for route in temp:
    red_edges = []
    G = nx.Graph()
    for k,val in adj_list.items():
        for i in val:
            G.add_edge(k,i)
    
    for i in range(len(route)-1):
        red_edges.append((route[i],route[i+1]))

    edge_colors = ['black' if not edge in red_edges else 'red' for edge in G.edges()]
    pos=nx.spring_layout(G)
    nx.draw_networkx(G,pos,node_size=1200,edge_color=edge_colors,edge_cmap=plt.cm.Reds)
    plt.show()