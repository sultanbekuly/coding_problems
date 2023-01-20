#Sum Lists: You have two numbers represented by a linked list, where each node contains a single
#digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
#function that adds the two numbers and returns the sum as a linked list.
#EXAMPLE
#Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
#Output: 2 -> 1 -> 9. That is, 912.
#FOLLOW UP
#Suppose the digits are stored in forward order. Repeat the above problem.
#EXAMPLE
#lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
#Output: 9 - > 1 -> 2. That is, 912.
#Hints: #7, #30, #71, #95, #109

# temp_var = 0
# We just need to sum the nodes data one by one (7+5+temp_var) = 12
#   write to output ll first digit 2(12)
#   write to temp_variable second digit 1(12)
#       use the temp_var in next sum

#TC - O(N) - N is length of the longest linked list
#SC - O(N) - due to res ll

#In the forward order case it would be harder.
#there is a need to reverse the ll and do the same

from LinkedList import LinkedList

def sum_lists(ll1,ll2):
    ll1.print()
    ll2.print()
    node1 = ll1.head
    node2 = ll2.head
    temp_var = 0

    res = node1.data + node2.data + temp_var #12
    digit_1 = res % 10 #2
    digit_2 = int((res/10)) ##1
    print(res, digit_1, digit_2)
    resll = LinkedList(digit_1)
    temp_var = digit_2
    node1 = node1.next
    node2 = node2.next
    while( not(node1 == None and node2 == None) ):
        data1 = 0  if node1==None else node1.data
        data2 = 0  if node2==None else node2.data 
        res = data1 + data2 + temp_var 
        digit_1 = res % 10 
        digit_2 = int((res/10)) 
        print(res, digit_1, digit_2)
        resll.append(digit_1)
        temp_var = digit_2
        node1 = None if node1==None else node1.next
        node2 = None if node2==None else node2.next
    if(temp_var) :
        resll.append(temp_var)
    return resll


myll1 = LinkedList(7)
myll1.add_multiple([1,6])
myll2 = LinkedList(5)
myll2.add_multiple([9,2])
sumll = sum_lists(myll1,myll2)
sumll.print()
#Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
#Output: 2 -> 1 -> 9. That is, 912.

#edge case:
#one var ll is begger than second one
myll1 = LinkedList(7)
myll1.add_multiple([1,6,1,3])
myll2 = LinkedList(5)
myll2.add_multiple([9,2])
sumll = sum_lists(myll1,myll2)
sumll.print()
#Input: (7-> 1 -> 6 -> 1 -> 3) + (5 -> 9 -> 2).That is,31617 + 295.
#Output: 2 -> 1 -> 9 ->1 -> 3. That is, 31912.

#edge case :
#remaining carry over value
myll1 = LinkedList(9)
myll1.add_multiple([9])
myll2 = LinkedList(9)
myll2.add_multiple([9])
sumll = sum_lists(myll1,myll2)
sumll.print()
#Input: (9-> 9) + (9 -> 9).That is, 99 + 99.
#Output: 8 -> 9 -> 1. That is, 198.




# Python Ternary Operator
#can_vote = True if age >= 18 else False

#The digits are stored in reverse order, such that the 1 's digit is at the head of the list
#number 123 reverse order - 3>2>1

#Suppose the digits are stored in forward order. Repeat the above problem
#number 123 forward order - 1>2>3

#sum_lists_followup
# Pad the shorter list with zeros
# Find sum
#   result = (result * 10) + n1.value + n2.
# Create new linked list
#   ll.add_multiple([int(i) for i in str(result)])