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

 #solution2
#          if len(s) != len(t):
#             return False

#         countS, countT = {}, {}

#         for i in range(len(s)):
#             countS[s[i]] = 1 + countS.get(s[i], 0)
#             countT[t[i]] = 1 + countT.get(t[i], 0)
#         return countS == countT
