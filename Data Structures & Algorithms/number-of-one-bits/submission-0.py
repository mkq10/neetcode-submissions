class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i, char in enumerate(bin(n)):
            if char == '1':
                count += 1
        return count