import copy
import random

def per(a):
    bn = str(a)
    import math
    F = []
    G = []
    X = []
    count = 1
    
    o = len(bn)
    for i in range(o):
        Y = bn[i]
        G.append(Y)
    for i in G:
        if i not in F:
            F.append(i)
            R = G.count(i)
            X.append(R)
    for i in X:
        count = count*(math.factorial(i))

    H = math.factorial(len(G))/count
    return(int(H))
def arrang(b):
    bn = str(b)
    import math
    F = []
    G = []
    X = []
    TBY = []
    count = 1
    
    o = len(bn)
    for i in range(o):
        Y = bn[i]
        G.append(Y)
    for i in G:
        if i not in F:
            F.append(i)
            R = G.count(i)
            X.append(R)
    for i in X:
        count = count*(math.factorial(i))

    H = int(math.factorial(len(G))/count)
    DDKS = []
    p=0
    while p ==0:
        Y = copy.copy(G)
        random.shuffle(Y)

        if DDKS.count(Y) == 0:
            DDKS.append(Y)
            if len(DDKS) == H:
                break
    
    for i in DDKS:
        stt = ''
        for j in i: 
            stt = stt + str(j)
        TBY.append(stt)
            
    return(TBY,H)
            
            
               

        
     
    
            
