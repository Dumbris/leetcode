package main
func smallerNumbersThanCurrent(nums []int) []int {
    res := make([]int, len(nums))
    for i, num1 := range nums {
        var c int = 0
        for j, num2 := range nums {
            if i == j {
                continue
            }    
            if num2 < num1 {
                c++
            }
        }
        res[i] = c
    }
    return res
}