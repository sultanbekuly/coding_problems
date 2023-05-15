class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        dict1 = {}
        dict2 = {}
        res1 = []
        res2 = []
        for i in nums1:
            if i not in dict1:
                dict1[i] = True
        for i in nums2:
            if i not in dict1 and i not in dict2:
                res2.append(i)
            if i not in dict2:
                dict2[i] = True
        for i in nums1:
            if i not in dict2 and i not in res1:
                res1.append(i)
        res = []
        res.append(res1)
        res.append(res2)
        return res
            
        
        