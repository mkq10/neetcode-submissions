class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_length = len(s)
        if s_length != len(t):
            return False

        for i in range(s_length):
            t = t.replace(s[i], "", 1)

        return len(t) == 0
        