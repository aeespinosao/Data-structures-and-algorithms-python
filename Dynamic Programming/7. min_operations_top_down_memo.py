def min_operations(s1: str, s2: str, index1: int, index2: int, memo: dict = {}) -> int:
    if index1 == len(s1):
        return len(s2) - index2
    if index2 == len(s2):
        return len(s1) - index1
    if s1[index1] == s2[index2]:
        return min_operations(s1, s2, index1 + 1, index2 + 1, memo)
    
    key = f"{index1}{index2}"
    if key not in memo:
        delete_sub = 1 + min_operations(s1, s2, index1 + 1, index2 + 1, memo)
        insert_sub = 1 + min_operations(s1, s2, index1 + 1, index2, memo)
        replace_sub = 1 + min_operations(s1, s2, index1 + 1, index2 + 1, memo)
        memo[key] = min(delete_sub, insert_sub, replace_sub)
    return memo[key]

print(min_operations('table', 'tbrles', 0, 0))
print(min_operations('table', 'tbrlest', 0, 0))