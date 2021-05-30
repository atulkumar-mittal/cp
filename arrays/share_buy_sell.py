def max_profit(a):
    print('Input array: {}'.format(a))
    mp = 0
    last_buy = 0
    i = 1
    while i < len(a):
        if a[i] < a[i - 1]:
            mp += a[i - 1] - a[last_buy]
            last_buy = i
        i += 1
    if last_buy != i - 1:
        mp += a[i - 1] - a[last_buy]
    print('max profit: {}'.format(mp))


# buy at bottom and sell at peak (
def max_profit_eff(a):
    mp = 0
    i = 1
    while i < len(a):
        if a[i] > a[i - 1]:
            mp += a[i] - a[i - 1]  # automatic buy at i-1
        i += 1
    print('max profit eff: {}'.format(mp))


max_profit([1, 5, 3, 2, 8, 12])
max_profit([30, 20, 10])
max_profit([10, 20, 20, 30])


max_profit_eff([1, 5, 3, 2, 8, 12])
max_profit_eff([30, 20, 10])
max_profit_eff([10, 20, 20, 30])
