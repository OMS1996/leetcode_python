# Optimal solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
	 
	Steps:
	 - creating an empty dictionary 
	 - subtracting current number from target number and storing it in a dictionary and storing its index
	 - if i find that a number later on in the array later that was equal to that number
	 That means they exist.
	- Get the index (value) of the element found in 
	  the dictonary which was the result of target - num , the current index
	
        """
        lib = {}
        for i,n in enumerate(nums):
            if n in lib:
                return [lib[n],i]
            lib[target - n] = i
        return []



# Solution 1: This Answer is BigO(NlogN)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # getting the SIZE
        n = len(nums)

        # Sorted array Big O(nlogn)
        sort_arr = sorted(nums)

        # Starting
        i = 0

        # last index.
        j = n-1

        # Getting the actual values.
        while(n > i and j > 0):
            if i != j:
                tot = sort_arr[i] + sort_arr[j]
                if tot == target:
                    break
                if tot < target:
                    i += 1
                if tot > target:
                    j -= 1

        # Saving some memory
        lst = [None,None]

        # Getting the index
        for k in range(len(nums)):
            if nums[k] == sort_arr[i] and lst[0] == None:
                lst[0] = k
            elif nums[k] == sort_arr[j]:
                lst[1] = k
        return lst

        
        
# Solution 2 to find ALL OF THEM all the pair sums
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 20:42:53 2020

@author: omarm
"""
nums = [3,2,4]
target = 6

nums = [3,3]

def twoSum(arr, k):
    # Seen and output sets
    seen = set()
    output = set()
    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num,target),max(num,target)))
    arr_lst = list(output)
        
    
    return arr_lst
    
                
                
        
        