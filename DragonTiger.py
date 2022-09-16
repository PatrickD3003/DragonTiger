import random
import math
import itertools
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
A = [0,1]
AT = []
digit_combination = 10
B = list(itertools.combinations_with_replacement(A, digit_combination))
n = pow(2, digit_combination)
lawan = [0,0,1,1,1,0,0,0,1,0,1,0,0,0,0,2,0,1,0,0,0,0,0,1,1,0,0,2,0,0,0,0,0,0,1,0,1,1,1,1,1,1,0,1,0,2,0,1,1,1,1,0,0,0,2,1,1,0,1,0,1,1,1,1,0,2,0,1,0,1,0,0,0,0,1,0,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,2,0,2,1,0,1,1,1,0,0,0,0,1,1,0,1,0,0,0,0,0,1,0,0,2,0,1,0,1,0,1,1,1,0,0,1,0,2,1,0,1,1,1,1,1,1,1,1,0,0,0,1]
lawanRandom = []
summary = [[] for _ in range(n)] 
def countGenerator():
    global A,AT
    for i in B:
        C = itertools.permutations(i)
        for j in list(C):
            if j not in AT:
                AT.append(j)
                continue
            else:
                continue

def compare(siapa):
    i = 0
    j = 0 
    k = 0   
    match = 0
    while True:
        
        if i > len(AT)-1:
            break
        if ( k > len(siapa)-1 ) or ( j > 4 ) :
                #print(f"kombinasi ke {i+1}{AT[i]}, banyak match {match}, kelar di {k} WIN THE GAME")
                summary[i].append([match,k])
                i += 1
                j = 0
                k = 0
                match = 0
                continue
        
        #kalo match
        if AT[i][j] == siapa[k]:
            j = 0
            k += 1
            match += 1
            # kalo win 
            continue
        #kalo gak match
        elif AT[i][j] != siapa[k]:
            j += 1
            k += 1
            continue

def enemyGenerator():
    lawanRandom.clear()
    for i in range(144):
        jeruk = random.randint(0,1)
        lawanRandom.append(jeruk)



def summ():
    print("--------------SUMMARY:left =  total match, right = lokasi kelar----------------")
    for i,j in enumerate(summary):
        print(f"kombinasi nomor {i+1} {AT[i]} : {j}")

def datFrame():
    global summary
    # length max l = len(summary)-1 = 31
    # length max m = len(summary[0])-1
    MTCH = []
    KLR = []

    for l in range(len(summary)):
            for m in range(len(summary[0])):
                MTCH.append(summary[l][m][0])
                KLR.append(summary[l][m][1])
                if m == len(summary[0])-1:
                    dats = {
                        "match" : MTCH,
                        "kelar" : KLR
                    }
                    df = pd.DataFrame(dats)
                    DeValue = np.std(MTCH)
                    meValue = np.mean(MTCH)
                    print(f'kombinasi ke {l+1} , {AT[l]} Standard Deviation Value : {DeValue:.2f}, mean {meValue:.2f}')
                    print(df)
                    MTCH = []
                    KLR = []
                    continue
                else:
                    continue

def matplot():
    global summary
    MTCH_plt = []
    KLR_plt = []
    #add text
    for l in range(len(summary)):
        for m in range(len(summary[0])):
            MTCH_plt.append(summary[l][m][0])
            KLR_plt.append(summary[l][m][1])
            if m == len(summary[0])-1:

                plt.plot(MTCH_plt,'ro')
                plt.xlabel("nomer")
                plt.ylabel("TOTAL MATCH")
                plt.title(f"kombinasi ke {l+1}")
                plt.show()

                MTCH_plt = []
                KLR_plt = []
                continue
            else:
                continue


countGenerator()

#print(lawan)
compare(lawan)

for engen in range(10):
    enemyGenerator()
    #print(lawanRandom)
    compare(lawanRandom)





#summ()
datFrame()
matplot()