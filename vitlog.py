h = {"a":-2.322,"c":-1.737,"g":-1.737,"t":-2.322,"h":-1,"l":-1}
l = {"a":-1.737,"c":-2.322,"g":-2.322,"t":-1.737,"l":-0.737,"h":-1.322}

startH = -1
startL = -1

pattern = "ggcactgaa"

hp = [startH+h[pattern[0]]]
lp = [startL+l[pattern[0]]]

    

for pat in pattern[1:]:
    xh = h[pat] + max(hp[-1]+h['h'] , lp[-1]+l['h'])
    xl = l[pat] + max(hp[-1]+h['l'] , lp[-1]+l['l'])
    
    hp.append(xh)
    lp.append(xl)


def printPath():
    for i,j in zip(hp,lp):
        if i > j:
            print('H',end=' ')
        else:
            print('L',end=' ')
            

print(2**max(lp[-1],hp[-1]))

printPath()