class Item:
    def __init__(self, profit: int, weight: int) -> None:
        self.profit = profit
        self.weight = weight
        
def z0_knapsack(items: list, capacity: int, current_index: int, memo: dict = {}):
    if capacity <= 0 or len(items) == 0 or len(capacity) != len(items):
        return 0
    numberOfRows = len(items) + 1
    dp = [[None for i in range(capacity+2)] for j in range(numberOfRows)]
    for i in range(numberOfRows):
        dp[i][0] = 0
    for i in range(capacity+1):
        dp[numberOfRows-1][i] = 0
    for row in range(numberOfRows-2, -1, -1):
        for column in range(1,capacity+1):
            profit1 = 0
            profit2 = 0
            if capacity[row] <= column:
                profit1 = items[row] + dp[row + 1][column - capacity[row]]
            profit2 = dp[row + 1][column]
            dp[row][column] = max(profit1, profit2)
    return dp[0][capacity]

mango = Item(31,3)
apple = Item(26,1)
orange = Item(17,2)
banana = Item(72,5)

items = [mango, apple, orange, banana]

print(z0_knapsack(items, 7, 0))