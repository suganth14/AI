import pyit2fls as pt2
import numpy as np
import matplotlib.pyplot as plt

domain = np.linspace(0,287,287)


def fuzzyTri(A,x):
    return max(min((x-A[0])/(A[1]-A[0]),(A[2]-x)/(A[2]-A[1])),0)

def fuzzyTra(A,x):
    return max(min((x-A[0])/(A[1]-A[0]),1,(A[-1]-x)/(A[-1]-A[-2])),0)


def createPlot(str1):
    NL_function = pt2.trapezoid_mf(domain, [-61,-31,31,61,1])
    NM_function = pt2.tri_mf(domain, [31,61,95,1])
    NS_function = pt2.tri_mf(domain, [61,95,127,1])
    ZE_function = pt2.tri_mf(domain, [95,127,159,1])
    PS_function = pt2.tri_mf(domain, [127,159,191,1])
    PM_function = pt2.tri_mf(domain, [159,191,223,1])
    PL_function = pt2.trapezoid_mf(domain,[191,223,265,268,1])
    
    plt.figure()
    plt.plot(domain,NL_function,label = "NL")
    plt.plot(domain,NM_function,label = "NM")
    plt.plot(domain,NS_function,label = "NS")
    plt.plot(domain,ZE_function,label = "ZE")
    plt.plot(domain,PS_function,label = "PS")
    plt.plot(domain,PM_function,label = "PM")
    plt.plot(domain,PL_function,label = "PL")
    plt.grid(True)
    plt.legend()
    plt.xlabel(str1)
    plt.ylabel("Degree Of Membership")
    plt.show()


def fuzzy(sd,ac,speed_diff,acc):
    val1 = None
    val2 = None
    
    if(len(speed[sd])==3):
        val1 = fuzzyTri(speed[sd], speed_diff)
    else:
        val1 = fuzzyTra(speed[sd], speed_diff)
    
    if(len(accel[ac])==3):
        val2 = fuzzyTri(accel[ac], acc)
    else:
        val2 = fuzzyTra(accel[ac], acc)
    
    return min(val1,val2)

def get_trapA(a,b,c,d,h):
    return (1/2)*(c-b + d-a)*h

def get_intersection(x1,y1,x2,y2,a):
    m = (y2-y1)/(x2-x1)
    x = (a-y1)/float(m) + x1
    return x

def de_fuzzy(val,A):
    # A = ["PS","PM"]
    num = 0
    denom = 0
    if(val==0):
        return
    i=0
    for key in A:
        arr = throttle[key]
        a = arr[0]
        b = get_intersection(arr[0],0,arr[1],1,val[i])
        c = get_intersection(arr[1],1,arr[2],0,val[i])
        d = arr[2]
        denom+=get_trapA(a,b,c,d,val[i])
        num+=(get_trapA(a,b,c,d,val[i])*((d+a)//2))
        i+=1
    return num/denom
        
    
    

speed = {
    "NL" : [-30,0,31,61],
    "NM" : [31,61,95],
    "NS" : [61,95,127],
    "ZE" : [95,127,159],
    "PS" : [127,159,191],
    "PM" : [159,191,223],
    "PL" : [191,223,255,287]
       }


accel = {
    "NL" : [-30,0,31,61],
    "NM" : [31,61,95],
    "NS" : [61,95,127],
    "ZE" : [95,127,159],
    "PS" : [127,159,191],
    "PM" : [159,191,223],
    "PL" : [191,223,255,287]
       }

throttle = {
    "NL" : [-30,0,31,61],
    "NM" : [31,61,95],
    "NS" : [61,95,127],
    "ZE" : [95,127,159],
    "PS" : [127,159,191],
    "PM" : [159,191,223],
    "PL" : [191,223,255,287]
    }

rules_list = [['NL','ZE','PL'],
['ZE','NL','PL'],
['NM','ZE','PM'],
['NS','PS','PS'],
['PS','NS','NS'],
['PL','ZE','NL'],
['ZE','NS','PS'],
['ZE','NM','PM']]

speed_diff = 100
acc = 70

createPlot("Normalized Speed Difference")
createPlot("Normalized Acceleration")
createPlot("Normalized Throttle Control")

#print(fuzzy("ZE","NM",speed_diff,acc),[])
A = []
val = []
for i in rules_list:
    if fuzzy(i[0],i[1],speed_diff,acc) > 0:
        val.append(fuzzy(i[0],i[1],speed_diff,acc))
        A.append(i[2])

print(A)        
print(de_fuzzy(val,A))
