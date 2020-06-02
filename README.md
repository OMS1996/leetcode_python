# Data-Structures-and-Algorthims

 Strategies that i have gathered
---------------------------------

- Arrays
  - Dictionary counter
  - Sort and then sort it out
  - Total sum as an indicator.
  - Arthemetic/ geometric sequence
    - Sum Arthemetic sequence with a difference of 1: l*(l+1)//2
    - Sum Arthemtic sequence in general = Number of elements * ( (first element + last element) / 2 )
    - Finding the nth element in an arthemetic sequence an=a1+(n−1)d .
    - Sum geometric sequence Sn=a1*(1−rn)/1−r,r≠1 
    - Finding the nth element in a geoemtric sequence an = a1*r**n−1
  - Seen / output : if you have seen this before add it to the output if 'NOT' add it to the seen
    - Example:
              
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
                  
  - Have i seen whats left of of you ?                     
      - Example:
      
      lib = {}
      
      for i,n in enumerate(nums):
          
          if n in lib:
          
               return [lib[n],i]
      
          lib[target - n] = i
      
      return []

 - XOR : Exclusive OR : if it is present in one but not present in the other
 
 - Cumulative & overall indicators
    * in the event where you have to find the fitness of a sequence (lets say total sum of a sequence), create a cumulative 
    that compares all what we have right now to what we have now and before, Once you chose the variable with the best local fitness
    compare it to the global fitness and from then on out repeat the process iteratively until you find the best global value
    for a sequence of numbers, remember that convergence only happens when you compare.
    * Example code:
                           """
                           Created on Wed May 27 22:34:13 2020
                           @author: omar
                           Finding the largest subarray in a sequence.
                           """
                           nums = [-2,1,-3,4,-1,2,1,-5,4]
                           def maxSubArray(nums):

                               n = len(nums) # Length
                               # Base case
                               if n==0:
                                   return 0

                               # Sentinels
                               sumed = 0
                               max_sum = float('-inf')

                               # BigO(N)
                               for i in range(n):    

                                   if sumed+nums[i] >= nums[i]:
                                       sumed = sumed+nums[i]
                                   else:
                                       sumed = nums[i]        

                                   if sumed >= max_sum:
                                       max_sum = sumed

                               return max_sum
 - Note,The double while is not N^2 if you continue on with the same iterator:
      On that not we can create two pointers based of the two while loops as such
          
          def reverseString(s):
    """
    :type s: str
    :rtype: str
    """
    n = len(s)
    words = list()
    i = 0
    while i < n:
        if s[i] != ' ':
            word_start = i
            while i < n and s[i] != ' ':
                i += 1
            words.append(s[word_start:i])
        i += 1
        
    return " ".join(reversed(words))
                
        
                
            
     







   










 
