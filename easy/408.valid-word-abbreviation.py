
"""
"internationalization"
 ^
"i12iz4n" 


 ^
 
 if is digit, read it into buffer.
 if letter and buffer not empty, -> move i to num, reset num
"""

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        l = len(word)
        current_num = ""
        while i < l and j < len(abbr):
            if abbr[j].isnumeric():
                if len(current_num) == 0 and int(abbr[j]) == 0: #has leading zeros
                    return False
                current_num += abbr[j]
                j += 1
                continue
            else:
                if len(current_num) > 0: #First letter after digits
                    #print(current_num)
                    i += int(current_num)
                    if i >= len(word): return False
                    current_num = ""
                if abbr[j] != word[i]:
                    return False
            i += 1
            j += 1
        if len(current_num) > 0:
            i += int(current_num)
        return i == len(word) and j == len(abbr)
                
        