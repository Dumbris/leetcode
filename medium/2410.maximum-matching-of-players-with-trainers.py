class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        res = 0
        i,j = 0,0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                res += 1
                j += 1
            i += 1
        return res