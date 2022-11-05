package main
func runningSum(nums []int) []int {
    res := make([]int,len(nums))
    var sum int = 0
    for i, n := range nums {
        if i == 0 {
            res[i] = n
            sum = n
            continue
        }
        sum = sum + n
        res[i] = sum
        
    }
    
    return res
}