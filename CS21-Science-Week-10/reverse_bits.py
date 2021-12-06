class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        k = bin(n)[2:].zfill(32)
        x = k[::-1]
        out= int(x,2)
        return out