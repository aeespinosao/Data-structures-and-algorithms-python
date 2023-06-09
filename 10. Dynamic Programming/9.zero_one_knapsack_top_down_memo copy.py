class Item:
    def __init__(self, profit: int, weight: int) -> None:
        self.profit = profit
        self.weight = weight
        
def z0_knapsack(items: list, capacity: int, current_index: int, memo: dict = {}):
    key = f"{current_index}{capacity}"
    if capacity <= 0 or current_index < 0 or current_index >= len(items):
        return 0
    elif key in memo:
        return memo[key]
    elif items[current_index].weight <= capacity:
        profit1 = items[current_index].profit + z0_knapsack(items, capacity-items[current_index].weight,current_index+1, memo)
        profit2 = z0_knapsack(items, capacity,current_index+1, memo)
        memo[key] = max(profit1, profit2)
        return memo[key]
    
    return 0

mango = Item(31,3)
apple = Item(26,1)
orange = Item(17,2)
banana = Item(72,5)

items = [mango, apple, orange, banana]

print(z0_knapsack(items, 7, 0))