import random
import math
import itertools
A = [0,1]
AT = []
B = list(itertools.combinations_with_replacement(A,5))
lawan = [0,0,1,1,1,0,0,0,1,0,1,0,0,0,0,2,0,1,0,0,0,0,0,1,1,0,0,2,0,0,0,0,0,0,1,0,1,1,1,1,1,1,0,1,0,2,0,1,1,1,1,0,0,0,2,1,1,0,1,0,1,1,1,1,0,2,0,1,0,1,0,0,0,0,1,0,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,2,0,2,1,0,1,1,1,0,0,0,0,1,1,0,1,0,0,0,0,0,1,0,0,2,0,1,0,1,0,1,1,1,0,0,1,0,2,1,0,1,1,1,1,1,1,1,1,0,0,0,1]
lawanRandom = []
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
                print(f"kombinasi ke {i+1}{AT[i]}, banyak match {match}, kelar di {k} WIN THE GAME")
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
                print(f"kombinasi ke {i+1}{AT[i]}, banyak match {match}, kelar di {k}")
                i += 1
                j = 0
                k = 0
                match = 0
                continue
            elif j > 4 and k > len(siapa)-1:
                print(f"kombinasi ke {i+1}{AT[i]}, banyak match {match}, kelar di {k}")
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


countGenerator()

print(lawan)
compare(lawan)
for ex in range(11):
    enemyGenerator()
    print(lawanRandom)
    compare(lawanRandom)



