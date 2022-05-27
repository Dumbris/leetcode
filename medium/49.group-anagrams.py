from collections import defaultdict
import string

letter2id = {ch:i for i,ch in enumerate(string.ascii_lowercase)}

class Solution:
    def hash_str(self, s:str)->Tuple:
        res = [0] * len(letter2id)
        for ch in s:
            res[letter2id[ch]] += 1
        return tuple(res)
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)
        for s in strs:
            _hash = self.hash_str(s)
            h[_hash].append(s)
        return [v for k,v in h.items()]
            
        
        