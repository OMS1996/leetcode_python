def gcd(a,b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a
gcd(105,147) #21