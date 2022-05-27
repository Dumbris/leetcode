class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])

        # A B C E
        #     ^
        # S F C S
        #
        # A D E E
        #
        #ABC
        # r 0
        # c 1
        # i 2

        def dfs(r, c, word, i, seen):
            if i == len(word)-1:
                return True
            seen.add((r,c))
            if r-1 >= 0 and (r-1,c) not in seen and board[r-1][c] == word[i+1]:
                if dfs(r-1, c, word, i+1, seen): return True
            if r+1 < R and (r+1,c) not in seen and board[r+1][c] == word[i+1]:
                if dfs(r+1, c, word, i+1, seen): return True
            if c-1 >= 0 and (r,c-1) not in seen and board[r][c-1] == word[i+1]:
                if dfs(r, c-1, word, i+1, seen): return True
            if c+1 < C and (r,c+1) not in seen and board[r][c+1] == word[i+1]:
                if dfs(r, c+1, word, i+1, seen): return True        
            seen.remove((r,c))
            return False
            


        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0]:
                    seen = set()
                    if dfs(r,c,word, 0, seen):
                        return True
        return False
        