import random
import math
import itertools
import pandas as pd
import numpy as np
A = [0,1]
AT = []
B = list(itertools.combinations_with_replacement(A,5))
lawan = [0,0,1,1,1,0,0,0,1,0,1,0,0,0,0,2,0,1,0,0,0,0,0,1,1,0,0,2,0,0,0,0,0,0,1,0,1,1,1,1,1,1,0,1,0,2,0,1,1,1,1,0,0,0,2,1,1,0,1,0,1,1,1,1,0,2,0,1,0,1,0,0,0,0,1,0,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,2,0,2,1,0,1,1,1,0,0,0,0,1,1,0,1,0,0,0,0,0,1,0,0,2,0,1,0,1,0,1,1,1,0,0,1,0,2,1,0,1,1,1,1,1,1,1,1,0,0,0,1]
lawanRandom = []
summary = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
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
        if k > len(siapa)-1:
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
            #kalo lose
            if j > 4:
                #print(f"kombinasi ke {i+1}{AT[i]}, banyak match {match}, kelar di {k}")
                summary[i].append([match,k])
                i += 1
                j = 0
                k = 0
                match = 0
                continue
            elif j > 4 and k > len(siapa)-1:
                #print(f"kombinasi ke {i+1}{AT[i]}, banyak match {match}, kelar di {k}")
                summary.append([match,k])
                if len(summary) == 32:
                    summary[i].append([match,k])
                i += 1
                j = 0
                k = 0
                match = 0
                continue
            else:
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
                print(f'kombinasi ke {l+1} , kombinasi {AT[l]}')
                print(df)
                MTCH = []
                KLR = []
                continue
            else:
                continue



"""
                datatoexcel = pd.ExcelWriter('DragonTigerBook.xlsx', engine='xlsxwriter')
                df.to_excel(datatoexcel, sheet_name = f'Sheet{1}')
                datatoexcel.save()
                """

""""
                MTCH = []
                KLR = []
            else:
                MTCH.append(summary[l][m][0])
                KLR.append(summary[l][m][1])
                


        dats ={
            "match" : MTCH,
            "kelar" : KLR
        }
"""

"""
---------------REFERENSI-------------------
data = {
    "babey" : [60,55,40],
    "weight": [50,43,23] 
}
df = pd.DataFrame(data)
datatoexcel = pd.ExcelWriter('DragonTigerBook.xlsx', engine='xlsxwriter')
df.to_excel(datatoexcel, sheet_name = f'sheet{1}')
datatoexcel.save()
"""


countGenerator()

#print(lawan)
compare(lawan)
for gengen in range(20):
    enemyGenerator()
    #print(lawanRandom)
    compare(lawanRandom)




#summ()
datFrame()
