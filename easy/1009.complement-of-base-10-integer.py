class Solution:
    def bitwiseComplement(self, n: int) -> int:
        #def bitwiseComplement(self, n: int) -> int:
        """The complement of an integer is the integer you get when you flip all the 0's to 1's 
        and all the 1's to 0's in its binary representation."""
        if n == 0:
            return 1

        binary = bin(n)[2:]

        complement = 0

        for i in range(len(binary)):
            if binary[i] == "0":
                complement += 2**(len(binary)-1-i)

        return complement
        