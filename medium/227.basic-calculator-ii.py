class Solution:
    def calculate(self, s: str) -> int:
        s += "+"
        def calc1():
            #print(q)
            if len(q) > 0 and q[-1] in set(["*","/"]):
                sign = q.pop()
                last_val = int("".join(last_digit))
                prev_val = q.pop()
                #print(q, prev_val, last_val)
                if sign == "*":
                    return prev_val*last_val
                elif sign == "/":
                    return prev_val//last_val
            else:
                return int("".join(last_digit))
        q = []
        last_digit = []
        last_sign = None
        for ch in s:
            if ch == " ":
                continue
            if ch.isdigit():
                last_digit.append(ch)
            else:
                if len(last_digit) > 0:
                    q.append(calc1())
                    last_digit = []
                q.append(ch)
        q.pop()
        res = 0
        last_op = None
        for i in q:
            if i in set(["+", "-"]):
                last_op = i
            else:
                if not last_op:
                    res = i
                else:
                    res = res + i if last_op == "+" else res - i
                
        return res