def isValidSubsequence(array, sequence):
	
	# Lengths.
	n = len(array)
	l = len(sequence)
	
	# Sentinels.
	i = 0
	j = 0
	
	# Base Case.
	if l > n:
		return False
	
	while i < n and j < l:
		if array[i] == sequence[j]:
			j += 1
		i += 1
	 
	return l == j
		
	
	#####################
	
def isValidSubsequence(array, sequence):
    
    seqIdx = 0
	
	for value in array:
		if seqIdx == len(sequence):
			return True
		if sequence[seqIdx] == value:
			seqIdx += 1
	return seqIdx == len(sequence)

	
		
	###########################
	
	
	
	
	
	
	
	
	
	
