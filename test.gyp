# print(12345%10)
# print(12345/10)

# print(1234%10)
# print(1234/10)

# print(123%10)
# print(123/10)

# print(12%10)
# print(12/10)

# print(1%10)
# print(1/10)

a = [5, 7, 8, 9, -1, 3]

prefixSum = []
print("prefixSum:",prefixSum)
for i in range(len(a)):
    prefixSum.append(a[i])
    if (i > 0): 
        prefixSum[i] += prefixSum[i - 1]
print(a)
print(prefixSum)
