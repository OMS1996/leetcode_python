# Solution 1

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        n = len(nums)
        for i in range(n+1):
            total += i
            if i == n:
                break
            total -= nums[i]

        return total

# Solution 2 using arthemetic sequence

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
	l = len(nums)
	s = l*(l+1)//2
	return s-sum(nums)

# Solution 3: XOR
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        n = len(nums)+1
        nums1 = [i for i in range(n)]
        for num in nums1+nums:
            result ^= num
        return result
        
