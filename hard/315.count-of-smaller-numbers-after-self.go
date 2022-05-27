func countSmaller(nums []int) []int {
    res := make([]int, len(nums))
    var prev int 
    var prev_c int
    for i, num1 := range nums {
        var c int = 0
        if num1 == prev {
            res[i] = prev_c
            continue
        } 
        for _, num2 := range nums[i:] {
            if num2 < num1 {
                c++
            }
        }
        res[i] = c
        prev = num1
        prev_c = c
    }
    return res
}