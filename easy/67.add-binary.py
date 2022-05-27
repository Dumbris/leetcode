class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = 0 #
        l = max(len(a), len(b))
        carry = 0
        res = []
        while i < l:
            a_bit = int(a[len(a) - i - 1]) if len(a) > i else 0
            b_bit = int(b[len(b) - i - 1]) if len(b) > i else 0
            
            s = a_bit + b_bit + carry
            #print(int(a[len(a) - i - 1]), int(b[len(b) - i - 1]), res, s, a_bit, b_bit, carry)
            if s < 2:
                res.append(str(s))
                carry = 0
            elif s == 3:
                res.append('1')
                carry = 1
            else:
                res.append('0')
                carry = 1
            #print(res, s, a_bit, b_bit, carry)
            i += 1
            
        if carry == 1:
            res.append('1')

        res.reverse()
        return "".join(res)
        