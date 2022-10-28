#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map1 = {}
        map2 = {}
        
        for val in range(len(s)):
            if s[val] in map1:
                map1[s[val]] += 1
            else:
                map1[s[val]] = 1
                

            if t[val] in map2:
                map2[t[val]] += 1
            else:
                map2[t[val]] = 1
                
        if map1 == map2:
            return True
        else:
            return False
