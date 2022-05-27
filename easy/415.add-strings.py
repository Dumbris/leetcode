class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l = max(len(num1), len(num2))
        res = []
        num1 = num1[::-1]
        num2 = num2[::-1]
        curry = 0
        for i in range(l):
            i1 = int(num1[i]) if len(num1) > i else 0
            i2 = int(num2[i]) if len(num2) > i else 0
            curry, r = divmod(curry + i1 + i2,10)
            res.append(str(r))
        if curry > 0:
            res.append(str(curry))
        return "".join(res[::-1])
        