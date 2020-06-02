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
