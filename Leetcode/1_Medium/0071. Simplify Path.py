"""
https://leetcode.com/problems/simplify-path/description/
Related Topics
String
Stack

TC: O(N)
SC: O(N)

"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        print(arr)
        # new_path = "/".join(arr)
        new_arr = []
        for i in arr:
            if(i!="" and i!="."):
                new_arr.append("/" + i)
            if(i==".."):
                if len(new_arr)!=0:
                    new_arr.pop()
                if len(new_arr)!=0:
                    new_arr.pop()

        # if(new_path == ""):
        #     new_path = "/"
        if len(new_arr)==0:
            new_arr.append("/")
        print(new_arr)
        return "".join(new_arr)