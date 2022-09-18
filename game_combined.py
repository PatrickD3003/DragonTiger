import random
import math
import itertools
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


all_loosers = []

lawan = [0,0,1,1,1,0,0,0,1,0,1,0,0,0,0,2,0,1,0,0,0,0,0,1,1,0,0,2,0,0,0,0,0,0,1,0,1,1,1,1,1,1,0,1,0,2,0,1,1,
1,1,0,0,0,2,1,1,0,1,0,1,1,1,1,0,2,0,1,0,1,0,0,0,0,1,0,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,2,0,2,1,0,1,1,1,0,0,0,
0,1,1,0,1,0,0,0,0,0,1,0,0,2,0,1,0,1,0,1,1,1,0,0,1,0,2,1,0,1,1,1,1,1,1,1,1,0,0,0,1]


def sum_generator():
    n = pow(2, game.digit_combination)
    sum_generator.summary = [[] for _ in range(n)] 

def count_generator():
    A = [0,1]
    B = list(itertools.combinations_with_replacement(A, game.digit_combination))
    count_generator.combination = []
    for i in B:
        C = itertools.permutations(i)
        for j in list(C):
            if j not in count_generator.combination:
                count_generator.combination.append(j)
                continue
            else:
                continue

def compare(siapa):
    i = 0
    j = 0 
    k = 0   
    match = 0
    while True:
        
        if i > len(count_generator.combination)-1:
            break
        if (k > len(siapa)-1) or (j > len(count_generator.combination[0])-1):
                sum_generator.summary[i].append([match, k])
                i += 1
                j = 0
                k = 0
                match = 0
                continue
        
        #kalo match
        if count_generator.combination[i][j] == siapa[k]:
            j = 0
            k += 1
            match += 1
            # kalo win 
            continue
        #kalo gak match
        elif count_generator.combination[i][j] != siapa[k]:
            j += 1
            k += 1
            continue

def enemy_generator():
    enemy_generator.lawan_random = []
    for i in range(144):
        random_generator = random.randint(0,1)
        enemy_generator.lawan_random.append(random_generator)

def data_frame():
    global all_loosers
    # length max l = len(summary)-1 = 31
    # length max m = len(summary[0])-1
    MTCH = []
    KLR = []
    LSR = 0
    looser_value = 0
    for l in range(len(sum_generator.summary)):
            for m in range(len(sum_generator.summary[0])):
                MTCH.append(sum_generator.summary[l][m][0])
                KLR.append(sum_generator.summary[l][m][1])

                if sum_generator.summary[l][m][0] < game.define_looser:
                    LSR += 1

                if m == len(sum_generator.summary[0])-1:
                    dats = {
                        "match" : MTCH,
                        "kelar" : KLR
                    }
                    df = pd.DataFrame(dats)
                    DeValue = np.std(MTCH)
                    meValue = np.mean(MTCH)

                    looser_value = LSR / len(sum_generator.summary[0]) * 100
                    all_loosers.append(looser_value)


                    print(f'kombinasi ke {l+1} , {count_generator.combination[l]} Standard Deviation Value : {DeValue:.2f}, mean {meValue:.2f}')
                    print(f'looser percentage = {looser_value:.2f}%, {LSR} looser out of {game.number_of_matches+1} matches')
                    print(df)
                    MTCH = []
                    KLR = []
                    looser_value = 0
                    LSR = 0
                    continue
                else:
                    continue


def math_plot():
    MTCH_plt = []
    KLR_plt = []
    #add text
    for l in range(len(sum_generator.summary)):
        for m in range(len(sum_generator.summary[0])):
            MTCH_plt.append(sum_generator.summary[l][m][0])
            KLR_plt.append(sum_generator.summary[l][m][1])
            if m == len(sum_generator.summary[0])-1:

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

def capital_binom():
    goal_money = int(input("input your income goal ="))
    bet_money = int(input("input your betting amount ="))
    game.digit_combination = int(input("input how many digit ur combination ="))
    adder_capital = 0
    capital = 0
    match_amount = goal_money / bet_money
    for i in range(game.digit_combination):
        adder_capital = bet_money * pow(2, i)
        capital += adder_capital

    one_trial_success = (pow(2, game.digit_combination)-1) / pow(2, game.digit_combination)
    binom_calc = pow(one_trial_success, match_amount) * 100
    print()
    print(f"{goal_money:,} income goal, {bet_money:,} betting amount, {game.digit_combination} digit combination")
    print(f"{capital:,} capital, {match_amount:.2f} match, with {binom_calc:.2f}% success rate")
    
def mean_lost():
    global all_loosers
    mean_loosers = np.mean(all_loosers)
    print(f"{mean_loosers:.2f}% lose mean, {100-mean_loosers:.2f}% win mean")

def matches_engine():
    compare(lawan)
    for i in range(game.number_of_matches):
        enemy_generator()
        compare(enemy_generator.lawan_random)

def game():
    while True:
        opening = input("input '0' for binomial calculator, '1' for game simulation, any other key to exit =")
        if opening == "0":
            capital_binom()
            continue
        elif opening == "1":
            game.digit_combination = int(input("input digit combination ="))
            game.define_looser = int(input("input looser number ="))
            game.number_of_matches = int(input("input number of simulation match ="))
            sum_generator()
            count_generator()
            matches_engine()
            game_option = input("input '0' for activating math plot, '1' for dataframe only , any other key to exit=")
            if game_option == "0":
                data_frame()
                math_plot()
                sum_generator.summary = []
                continue
            elif game_option == "1":
                data_frame()
                mean_lost()
                sum_generator.summary = []
                continue
        else:
            break

game()
