def common_subsequence(s1: str, s2: str, index1: int, index2: int):
    if index1==len(s1) or index2==len(s2):
        return 0
    if s1[index1]==s2[index2]:
        return 1 + common_subsequence(s1, s2, index1+1, index2+1)
    
    op1 = common_subsequence(s1, s2, index1, index2+1)
    op2 = common_subsequence(s1, s2, index1+1, index2)
    
    return max(op1, op2)

print(common_subsequence('elephant', 'eretpat', 0, 0))