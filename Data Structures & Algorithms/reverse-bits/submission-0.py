class Solution:
    def reverseBits(self, n: int) -> int:
        b = ""
        for i in range(32):
            if n & (1 << i):
                b += "1"
            else:
                b += "0"

        return int(b, 2)
