"""
https://leetcode.com/problems/valid-parentheses/description/
Related Topics
String
Stack
----------------

we need to use the stack
data will be added to the stack if it is opening bracket and will be deleted from it for closing bracket
if closing bracket not match with last item return False
if after string finished something in stack return False
else return True

Stack is LIFO
"""
#1<2<3<4<5
class Node:
    def __init__(self, bracket:str, prev):
        self.bracket  = bracket
        self.prev = prev

class Stack:
    # def __init__(self, bracket:str):
    def __init__(self):
        # the_node = Node(bracket)
        # self.tail = the_node
        self.tail = None


    def add(self, bracket:str):
        the_node = Node(bracket, self.tail)
        self.tail = the_node
    
    def pop(self):
        self.tail = self.tail.prev
    

class Solution:
    def isValid(self, s: str) -> bool:
        def get_opening_bracket(b:str) -> str:
            if(b == ')'):
                return '('
            if(b == '}'):
                return '{'
            if(b == ']'):
                return '['
            
        stack = Stack()
        for i in s:
            if(i in [ '(', '{', '[' ]):
                stack.add(i)
            elif(i in [ ')', '}', ']' ]):
                if stack.tail == None:
                    return False
                if(stack.tail.bracket == get_opening_bracket(i) ):
                    stack.pop()
                else:
                    return False
                
        if stack.tail != None:
            return False
        return True

            



