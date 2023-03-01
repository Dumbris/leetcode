class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = s[::-1]
        t = t[::-1]
        def remove(_str):
            bs_count = 0
            res = []
            for ch in _str:
                if ch == '#':
                    bs_count += 1
                elif bs_count > 0:
                    bs_count -= 1
                else:
                    res.append(ch)
            return "".join(res)

        return remove(s) == remove(t)

