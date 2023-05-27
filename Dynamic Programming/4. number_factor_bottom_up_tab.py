
def number_factor(n: int):
    tb = [1, 1, 1, 2]
    for i in range(4, n+1):
        tb.append(tb[i-1]+tb[i-3]+tb[i-4])
    return tb[n]

memo = {}
print(number_factor(5, memo))