
def number_factor(n: int, memo: dict):
    if n in (0,1,2):
        return 1
    elif n == 3:
        return 2
    elif n in memo:
        return memo[n]
    else:
        sub1 = number_factor(n-1, memo)
        sub2 = number_factor(n-3, memo)
        sub3 = number_factor(n-4, memo)
        memo[n] = sub1 + sub2 + sub3
        return memo[n]

memo = {}
print(number_factor(5, memo))