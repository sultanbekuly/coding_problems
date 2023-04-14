"""
https://leetcode.com/problems/longest-palindromic-subsequence/
Related Topics
String
Dynamic Programming


Two pointers one fom start-> second from <-end
right pointer tries to match with the left one 

then we can do in the backward

"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # Initialize a 2D dp array to store the length of the longest palindromic subsequence
        dp = [[0] * n for _ in range(n)]

        # Base case: every character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1

        # Iterate through the dp array from bottom up, starting with substrings of length 2
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                if s[i] == s[j]:
                    # If the characters at i and j are the same, then the length of the longest palindromic subsequence is
                    # 2 plus the length of the longest palindromic subsequence in the substring s[i+1:j-1]
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    # If the characters at i and j are different, then the length of the longest palindromic subsequence is
                    # the maximum of the length of the longest palindromic subsequence in the substring s[i:j-1] and the
                    # length of the longest palindromic subsequence in the substring s[i+1:j]
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])

        # Return the length of the longest palindromic subsequence in the entire string
        return dp[0][n-1]


        print(s)
        arr = list(s)
        print(arr)
        left = 0
        right = len(arr)-1
        counter = 0
        left_chp = left
        right_chp = right   #check point
        move_right = True #False > move left
        #if note same left will try to find
        while True:
            print(">",left,right)
            # if right-left <= 2:
            if right==left:
                print("break", counter)
                counter = counter*2
                counter += 1
                print("break", counter)
                break
            if left>right:
                print("break", counter)
                counter = counter*2
                print("break", counter)
                break

            if(arr[left] == arr[right]):
                counter += 1
                left += 1
                right -= 1
            else:
                right -= 1

        return counter