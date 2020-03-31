def fib(n):
    ''' This is a fibinoucii sequence number that assumes you start \
        from index zero and you include zero as the first element of the sequence.
    '''
    
    # Initializing
    arr = []
    
    # Appending the base values.
    arr.append(0)
    arr.append(1)
    
    
    for i in range(2,n+1):
        arr.append((arr[i-1] + arr[i-2]))
        
        
    return arr