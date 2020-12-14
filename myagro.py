def get_days_of_power(R1, D1, R2, D2, R3, D3, K):
    loans = [(R1, D1), (R2, D2), (R3, D3)]
    sorted_loans = sorted(loans, key=lambda l: l[1])
    median_d = sorted_loans[1][1]
    median_r = sorted_loans[1][0]
    min_r = sorted_loans[0][0]
    min_d = sorted_loans[0][1]
    max_r = sorted_loans[2][0]
    max_d = sorted_loans[2][1]
    total_days = 0
    balance = K
    num_distinct = len(set([min_d, median_d, max_d]))
    if(num_distinct > 2):
        num_first_range = len(list(range(min_d, median_d)))
        num_second_range = len(list(range(median_d, max_d)))
        num_third_range = None
        expected_days = (num_first_range, num_second_range, num_third_range)
        rates = (min_r, min_r+median_r, min_r+median_r+max_r)
        balance, total_days = handle_iter(
            balance, total_days, zip(expected_days, rates))
        return(total_days)

    elif(num_distinct == 2):
        if min_d == median_d:
            num_first_range = len(list(range(min_d, max_d)))
            num_second_range = None
            expected_days = (num_first_range, num_second_range)
            rates = (min_r+median_r, min_r+median_r+max_r)
            balance, total_days = handle_iter(
                balance, total_days, zip(expected_days, rates))
            return(total_days)
        else:
            num_first_range = len(list(range(min_d, median_d)))
            num_second_range = None
            expected_days = (num_first_range, num_second_range)
            rates = (min_r, min_r+median_r+max_r)
            balance, total_days = handle_iter(
                balance, total_days, zip(expected_days, rates))
            return(total_days)

    elif(num_distinct == 1):
        expected_days = (None,)
        rates = (min_r+median_r+max_r,)
        balance, total_days = handle_iter(
            balance, total_days, zip(expected_days, rates))
        return(total_days)


def handle_iter(balance, total_days, day_n_rates):
    for expected_days, rates in day_n_rates:
        if balance/rates < 1:
            break
        temp_balance, temp_covered_days = get_bal(
            balance, rates, expected_days)
        balance = temp_balance
        total_days = total_days+temp_covered_days
    return (temp_balance, total_days)


def get_bal(balance, rate, expected_days=None):
    actual_days = int(balance/rate)
    expected_days = actual_days if not expected_days else expected_days
    to_be_deducted = actual_days if actual_days < expected_days else expected_days
    balance = balance-rate*to_be_deducted
    return (balance, to_be_deducted)
