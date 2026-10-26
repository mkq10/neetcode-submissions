class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_a = set(s)
        set_b = set(t)
        return len(s) == len(t) and sorted(s) == sorted(t)