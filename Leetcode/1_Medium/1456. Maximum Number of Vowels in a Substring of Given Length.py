class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # arr = []
        # vowels = ['a','e','i','o','u']
        # res = 0
        # x = 0
        # for i in range(len(s)):
            
        #     if s[i] in vowels:
        #         arr.append(1)
        #         x += 1
        #     else:
        #         arr.append(0)
        #     # x = sum(arr[k*-1:])

        #     if()

        #     if res < x:
        #         res = x
        #     if res == k:
        #         return res 
        # # res = 0
        # # for i in range(k-1, len(s)):
        # #     # print(i,i-k+1, arr[i-k+1:i+1], s[i-k+1:i+1])
        # #     x = sum(arr[i-k+1:i+1])
        # #     if res < x:
        # #         res = x
        # #     if res == k:
        # #         return res            
        # return res

        s_list = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        cnt = 0
        for i in range(k):
            if s_list[i] in vowels:
                cnt = cnt + 1
        max_num = cnt
        for end in range(k,len(s)):
            start = end - k + 1
            if s_list[start-1] in vowels:
                cnt = cnt - 1
            if s_list[end] in vowels:
                cnt = cnt + 1
            max_num = max(max_num, cnt)
        return max_num        
        