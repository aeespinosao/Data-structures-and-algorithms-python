def min_operations(s1: str, s2: str, memo: dict = {}):
    for i1 in range(len(s1)+1):
        dictKey = str(i1)+'0'
        memo[dictKey] = i1
    for i2 in range(len(s2)+1):
        dictKey = '0'+str(i2)
        memo[dictKey] = i2
    
    for i1 in range(1,len(s1)+1):
        for i2 in range(1,len(s2)+1):
            if s1[i1-1] == s2[i2-1]:
                dictKey = str(i1)+str(i2)
                dictKey1 = str(i1-1)+str(i2-1)
                memo[dictKey] = memo[dictKey1]
            else:
                dictKey = str(i1)+str(i2)
                dictKeyD = str(i1-1)+str(i2)
                dictKeyI = str(i1)+str(i2-1)
                dictKeyR = str(i1-1)+str(i2-1)
                memo[dictKey] = 1 + min(memo[dictKeyD], min(memo[dictKeyI],memo[dictKeyR]))
    dictKey = str(len(s1))+str(len(s2))
    return memo[dictKey]

print(min_operations('table', 'tbrles'))
print(min_operations('table', 'tbrlest'))