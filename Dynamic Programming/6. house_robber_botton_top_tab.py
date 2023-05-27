def house_robber(houses: list, current_index: int) -> int:
    tb = [0] * (len(houses)+2)
    
    for i in range(len(houses)-1, -1, -1):
        tb[i] = max(houses[i] + tb[i+2], tb[i+1])
    return tb[0]

houses = [6, 7, 1, 30, 8, 2, 4]
print(house_robber(houses, 0))