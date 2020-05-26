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












 
