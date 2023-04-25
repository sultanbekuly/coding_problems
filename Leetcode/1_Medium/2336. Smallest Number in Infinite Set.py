"""
https://leetcode.com/problems/smallest-number-in-infinite-set/description/
Related Topics
Hash Table
Design
Heap (Priority Queue)

"""
class node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = node(1)
        self.greatest = self.smallest.val
        # print("init")
        # print(self.print_nodes())
        return None

    def popSmallest(self) -> int: #O(1)
        #delete first element
        num = self.smallest.val
        if self.smallest.next == None: #only one item in the list
            self.smallest.val += 1
            self.greatest += 1
        else:
            self.smallest  = self.smallest.next
        # print("}popSmallest", num)
        # print(self.print_nodes())
        return num

    def addBack(self, num: int) -> None:
        # print("}addBack:",num)
        # print(self.print_nodes())
        curr_node = self.smallest
        if num >= self.greatest:     #this number is not opened yet
            # print("addBack", "this number is not opened yet")
            # print(self.print_nodes())
            return None
        elif num < curr_node.val:        #1 < 4
            the_node = node(num)
            the_node.next = self.smallest
            self.smallest = the_node        #1->4
            # print("addBack", "elif num < curr_node.val:        #1 < 4")
            # print(self.print_nodes())
            return None
        else:
            #1->4; num:2
            prev_node = None
            while (curr_node is not None):
                # print("--",curr_node.val)
                if(curr_node.val == num):
                    # print("addBack", "if(curr_node.val == num):")
                    # print(self.print_nodes())
                    return None
                elif num < curr_node.val:        #2 < 4
                    the_node = node(num)
                    next_node = curr_node
                    the_node.next = next_node
                    prev_node.next = the_node
                    # print("addBack", "elif num < curr_node.val:        #2 < 4")
                    # print(self.print_nodes())
                    return None       
                prev_node = curr_node
                curr_node = curr_node.next
    
    # def print_nodes(self):
    #     arr = []
    #     node = self.smallest
    #     while( node != None ):
    #         arr.append( str(node.val) )
    #         node = node.next
    #     return "print_nodes:"+"->".join(arr)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)