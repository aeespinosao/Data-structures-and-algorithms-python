def house_robber(houses: list, current_index: int) -> int:
    if current_index >= len(houses): return 0
    
    steal_house =  houses[current_index] + house_robber(houses, current_index+2)
    skip_house = 0 + house_robber(houses, current_index + 1)
    
    return max(steal_house, skip_house)

houses = [6, 7, 1, 30, 8, 2, 4]
print(house_robber(houses, 0))