h = {"a":0.2,"c":0.3,"g":0.3,"t":0.2,"h":0.5,"l":0.5}
l = {"a":0.3,"c":0.2,"g":0.2,"t":0.3,"l":0.6,"h":0.4}


pattern = "ggca"
hp = [0.5*h[pattern[0]]]
lp = [0.5*l[pattern[0]]]

for pat in pattern[1:]:
    xh = hp[-1]*h[pat]*h['h'] + lp[-1]*h[pat]*l['h'] 
    xl = lp[-1]*l['l']*l[pat] + hp[-1]*l[pat]*h['l']
    hp.append(xh)
    lp.append(xl)
    
print(hp[-1]+lp[-1])