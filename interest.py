def simulate(opening_balance, rate, time):
    """doc"""
    new_rate = rate.strip().split()
    print(new_rate)
    if '%' in new_rate[0]:
        rate = float(new_rate[0][:-1])/ 100
    else:
        raise ValueError
    if "annually" in new_rate:
        new_time = time.days/360
        # amount = opening_balance * (pow((1 + rate), new_time))
        amount = opening_balance * (1 + rate)** (new_time)
        # CI = amount - opening_balance
        return amount
    elif "monthly" in new_rate:
        new_time = time.days/30
        amount = opening_balance * (1 + rate)**( new_time)
        #CI = amount - opening_balance
        return amount
    else:
        raise ValueError
    
