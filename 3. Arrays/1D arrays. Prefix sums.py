a = [5, 7, 8, 9, -1, 3]

prefixSum = []
for i in range(len(a)):
    prefixSum.append(a[i])
    if (i > 0): 
        prefixSum[i] += prefixSum[i - 1]
print(a)
print(prefixSum)