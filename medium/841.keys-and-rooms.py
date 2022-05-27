class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set()
        seen.add(0)
        def dfs(_key):
            if _key not in seen:
                seen.add(_key)
                for new_key in rooms[_key]:
                    dfs(new_key)
            
        for _key in rooms[0]: 
            dfs(_key)
        
        for i in range(len(rooms)):
            if i not in seen:
                return False

        return  True
        