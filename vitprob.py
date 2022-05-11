h = {"a":0.2,"c":0.3,"g":0.3,"t":0.2,"h":0.5,"l":0.5}
l = {"a":0.3,"c":0.2,"g":0.2,"t":0.3,"l":0.6,"h":0.4}

startH = 0.5
startL = 0.5

pattern = "ggcactgaa"

hp = [0.5*h[pattern[0]]]
lp = [0.5*l[pattern[0]]]

    

for pat in pattern[1:]:
    xh = h[pat] * max(hp[-1]*h['h'] , lp[-1]*l['h'])
    xl = l[pat] * max(hp[-1]*h['l'] , lp[-1]*l['l'])
    
    hp.append(xh)
    lp.append(xl)


def printPath():
    for i,j in zip(hp,lp):
        if i > j:
            print('H',end=' ')
        else:
            print('L',end=' ')
            
    
print("hp :",hp)
print("lp :",lp)
print(max(lp[-1],hp[-1]))

printPath()