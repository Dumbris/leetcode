package main
func twoSum(nums []int, target int) []int {
    l := len(nums)
    for i := 0; i < l-1; i++ {
        target2 := target - nums[i]
        for j := i+1; j < l; j++ {
            //fmt.Println(i,j, target2)
            if  target2 == nums[j] {
                return []int{i,j}
            }
        }
    }
    return nil
}