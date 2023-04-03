"""
https://leetcode.com/problems/boats-to-save-people/description/

Sort - people list

two pointers

TC: O(nLogn)
SC: O(1)
"""
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        L = 0
        R = len(people)-1
        answer = 0
        while(L<R):
            if(people[R] == limit):
                answer += 1
                R -= 1
            else: #less than limit
                if( limit - people[R] >= people[L]):
                    R -= 1
                    L += 1
                    answer += 1
                else:
                    R -= 1
                    answer += 1
        print(L,R)
        if(L==R): #increment for last val
            answer += 1
        return answer

"""
case:
    [3,2,2,1], 3
    [3,5,3,4], 5
edge cases: 
    [1,2], 3
    [2,2], 6
"""

#test = Solution()
#people = [3,2,2,1]
#limit = 3
#print(test.numRescueBoats(people, limit))


