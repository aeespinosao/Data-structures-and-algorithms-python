def house_robber(houses: list, current_index: int, memo: dict = {}) -> int:
    if current_index >= len(houses): return 0
    
    if houses[current_index] not in memo:
        steal_house =  houses[current_index] + house_robber(houses, current_index+2, memo)
        skip_house = 0 + house_robber(houses, current_index + 1, memo)
        memo[houses[current_index]] = max(steal_house, skip_house)
    return memo[houses[current_index]]

houses = [6, 7, 1, 30, 8, 2, 4]
print(house_robber(houses, 0))