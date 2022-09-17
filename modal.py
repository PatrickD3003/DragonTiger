def capital_binom():
    goal_money = int(input("input your income goal ="))
    bet_money = int(input("input your betting amount ="))
    digit_combination = int(input("input how many digit ur combination ="))

    match_amount = goal_money / bet_money
    capital = bet_money * pow(2, digit_combination - 1)

    one_trial_success = (pow(2, digit_combination)-1) / pow(2, digit_combination)
    binom_calc = pow(one_trial_success, match_amount) * 100
    print()
    print(f"{goal_money:,} income goal, {bet_money:,} betting amount, {digit_combination} digit combination")
    print(f"{capital:,} capital, {match_amount} match, with {binom_calc:.2f}% success rate")

while True:
    capital_binom()
    terminator = input("continue the program? (y/n)")
    if terminator == "y":
        continue
    elif terminator == "n":
        break

            
        

