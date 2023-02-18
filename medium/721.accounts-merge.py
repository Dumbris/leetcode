from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        h = defaultdict(list)
        seen = set()
        res = []
        for i, account in enumerate(accounts):
            name = account[0]
            for email in account[1:]:
                h[email].append(i)

        for i, account in enumerate(accounts):
            if i in seen:
                continue
            q = account[1:]
            person_emails = []
            while q:
                email = q.pop()
                person_emails.append(email)
                if len(h[email]) > 1:
                    for j in h[email]:
                        if j not in seen:
                            q.extend(accounts[j][1:])
                            seen.add(j)
            res.append([account[0]] + sorted(list(set(person_emails)), reverse=False))
        return res