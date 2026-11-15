class Solution:
    def reverseBits(self, n: int) -> int:
        bits = []
        for i in range(32):
            bit = (n >> i) & 1
            bits.append(bit)
        res = 0
        bit_value = 1
        for i in range(len(bits) - 1, -1, -1):
            curr_bit = bits[i]
            if curr_bit:
                res += bit_value
            bit_value *= 2
        return res
            

            
        