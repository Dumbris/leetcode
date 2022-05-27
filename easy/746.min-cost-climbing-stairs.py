"""
dp[i] - cost of i-th step

[1,100,1,1,1,100,1,1,100,1]
                   ^         

"""
#   [10, 15, 20]

#[0, 10, 15, 30]


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 2)
        cost.append(0)
        dp[1] = cost[0]
        for i in range(2,len(dp)): 
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i-1]
            i += 1
        #print(dp)
        return dp[-1]
        