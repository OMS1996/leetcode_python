nums1 = [1,2,3,4,5,6,7]
nums2 = [3,7,2,1,4,6]

# Solution 1 which is NlogN
def finder(nums1,nums2):
    
    n = len(nums1)
    
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    
    for i in range(n):
        if nums1[i] != nums2[i]:
            return nums1[i]
    
# Solution 2 which is N, it is Optimal
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 20:42:53 2020

@author: omarm
"""
nums1 = [1,2,3,4,5,6,7]
nums2 = [3,7,2,1,4,6]

        
def finder(nums1,nums2):
    
    total = 0
    
    n = len(nums1)
    
    for i in range(n):
        total += nums1[i]
        if n-1 > i:
            total -= nums2[i]
    return total
        
        
        
        
        
       
