# Solution 1 at 52 ms
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create sets S and T
        setS = set(s)
        setT = set(t)

        # Unique length
        s_set = len(setS)
        t_set = len(setT)

        if s_set != t_set:
            if s_set > t_set + 1 or s_set + 1 < t_set:
                return False

        # Actual length.
        s_len = len(s)
        t_len = len(t)

        # HashMap.
        sdic = {i:0 for i in setS}
        tdic = {i:0 for i in setT}


        for i in range(s_len):
            sdic[s[i]] += 1

        for i in range(t_len):
            tdic[t[i]] += 1

        # Removing the white space
        if ' ' in sdic:
            sdic.pop(' ')
        if ' ' in tdic:
            tdic.pop(' ')

        if sdic == tdic:
            return True
        else:
            return False

# Slightly better solution 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Removing white spaces.
        s = s.replace(' ','').lower()
        t = t.replace(' ','').lower()
        
        return sorted(s) == sorted(t)

# A better Solution 3 at 36 ms
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Removing white spaces.
        s = s.replace(' ','').lower()
        t = t.replace(' ','').lower()

        # Create sets S and T
        setS = set(s)
        setT = set(t)

        # Actual length.
        s_len = len(s)
        t_len = len(t)

        # Check before we start the process.
        if s_len != t_len:
            return False


        # HashMap.
        sdic = {i:0 for i in setS}
        tdic = {i:0 for i in setT}

        # Loop and add to the dictionary
        for i in range(s_len):
            sdic[s[i]] += 1
            tdic[t[i]] += 1

        print(sdic)
        print(tdic)
        if sdic == tdic:
            return True
        else:
            return False