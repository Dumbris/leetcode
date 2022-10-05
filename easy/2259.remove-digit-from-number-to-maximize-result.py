class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        number2 = [int(c) for c in number]
        idx = []
        for i,n in enumerate(number2):
            if n == int(digit):
                idx.append(i)
        max_res = 0
        for i in idx:
            new_n = []
            for j in range(len(number2)):
                if i != j:
                    new_n.append(str(number2[j]))
            max_res = max(max_res, int("".join(new_n)))
        return str(max_res)
            
        