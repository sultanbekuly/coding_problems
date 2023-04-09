#57. Insert Interval
#https://leetcode.com/problems/insert-interval/description/

#res_arr = []
#overlap_started = False
#iterate through intervals
#   #check if interval overlaps with newInterval
#   if overlap: update newInterval[min(..), max(..)], overlap_started = True
#   else: if overlap_started == False: res_arr.append interval
#           else: #it means overlapping finished 
#                  overlap_started = False
#                   res_arr.append --newInterval, interval
#if no overlapping ..

# corner case:
#intervals = [[6,7],[8,10],[12,16]], newInterval = [4,8] =>[[4,10],[12,16]]
#both newInterval[0] and [1] are not inside [6,7]
#against [6,7] inside of the (newInterval)[4,8]

#edge case: intervals =[]; newInterval =[5,7]

#edge case: [[3,4],[5,6]]; [1,2] or [7,8] 
#if its not overlapped, it means newInterval needs to be added to the start or to the end
#wrong assumption. It can be in somewhere middle but not overlapped:
#[[3,5],[12,15]] [6,6]


#TC - O(N) - N number of elements in intervals
#SC - O(N)
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if intervals == []:
            return [newInterval]
        
        res_arr = []
        overlap_started = False
        overlapped = False

        for interval in intervals:
            #check if interval overlaps with newInterval
            if( overlap(interval, newInterval) ):
                overlap_started = True
                overlapped = True
                newInterval[0] = min(newInterval[0],interval[0])
                newInterval[1] = max(newInterval[1],interval[1])
                # print("newInterval:", newInterval)
            else:
                if(overlap_started==False):
                    res_arr.append(interval)
                else:#it means overlapping finished 
                    overlap_started = False
                    res_arr.append(newInterval)
                    res_arr.append(interval)
        if(overlap_started == True):
            res_arr.append(newInterval)
        
        if(not(overlapped)): 
            res_arr = []   
            if(newInterval[1] < intervals[0][0]): # [1,2] | [[3,4],[5,6]] 
                res_arr = [newInterval] + intervals
            elif(newInterval[0] > intervals[-1][1]): # [7,8] | [[3,4],[5,6]] 
                res_arr = intervals + [newInterval]
            else:
                for i in range(1, len( intervals )):
                    # print(intervals[i-1][1],newInterval[0], 
                    #     newInterval[1],intervals[i][0])

                    if(intervals[i-1][1] < newInterval[0] and 
                        newInterval[1] < intervals[i][0]):
                        res_arr = intervals[:i] + [newInterval] + intervals[i:]
        return res_arr

def overlap(interval, newInterval) :
    #print(interval, newInterval)
    if( (interval[0]<=newInterval[0] and newInterval[0]<=interval[1]) or 
        (interval[0]<=newInterval[1] and newInterval[1]<=interval[1]) ):
        # print("C1")
        return True
    if( (newInterval[0]<=interval[0] and interval[0]<=newInterval[1]) or 
        (newInterval[0]<=interval[1] and interval[1]<=newInterval[1]) ):
        # print("C2")
        return True
    return False
    
test = Solution()
print(test.insert( [[1,3],[6,9]], [2,5] ))
#Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
#Output: [[1,5],[6,9]]

print(test.insert( [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8] ))
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

print(test.insert( [[3,4],[5,6]], [1,2] )) #[[1,2], [3,4], [5,6]] 

print(test.insert( [[3,4],[5,6]], [7,8]  )) #[[3,4], [5,6], [7,8]] 

print(test.insert( [[3,5],[12,15]], [6,6]  )) #[[3,5], [6,6], [12,15]]
