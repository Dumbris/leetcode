package main
func removeDuplicates(nums []int) int {
    n := 0
    for i, x := range nums {
        if i == 0 {
            nums[n] = x
		    n++
            continue
        }
	    if x != nums[n-1] {
		    nums[n] = x
		    n++
	    }
    }
    return n
    
}