class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def f(arr, tar, acc):
            #print(arr, tar, acc)
            if tar == 0:
                res.append(acc)
            if len(arr) == 0 or tar < 0:
                return
            for i in range(len(arr)):
                f(arr[i:], tar-arr[i], acc + [arr[i]])
        f(candidates, target, [])

        return res
        