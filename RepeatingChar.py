#sliding window
#Given a string s, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(self, s: str) -> int:
        #creating a set to eliminate duplicate elements
        charset = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            res = max(res, r - l + 1)
        return res
print(lengthOfLongestSubstring("abcabcbb"))
