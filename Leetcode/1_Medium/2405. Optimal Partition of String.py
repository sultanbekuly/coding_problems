"""
https://leetcode.com/problems/optimal-partition-of-string/description/
"""
"""
go through string s 
add char to dict and increment value

go through the dict
get max value

TC: O(n)
SC: O(n)
-> cannot pass this test case:
    "hdklqkcssgxlvehva"
"""

"""
go thorugh string s
    check char in dict (if not exists)
        add char to dict, value is current count
    else:
        check if value is equal to current count
        if so, increment count, assign new count
"""
class Solution:
    def partitionString(self, s: str) -> int:
        # mydict = {}
        # for i in s:
        #     if i in mydict:
        #         mydict[i] += 1
        #     else:
        #         mydict[i] = 1
        # max_val = 0
        # print(mydict)
        # for _, val in mydict.items():
        #     if(val>max_val):
        #         max_val = val
        # return max_val

        mydict = {}
        count = 1
        for i in s:
            if i in mydict:
                if mydict[i] == count:
                    count += 1
                    mydict[i] = count
                else:
                    mydict[i] = count
            else:
                mydict[i] = count
        return count
