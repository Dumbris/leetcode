impl Solution {
    pub fn move_zeroes(nums: &mut Vec<i32>) {
        let mut i = 0;
        let mut j = 0;
        while i < nums.len() {
            if nums[i] != 0 {
                nums.swap(j, i);
                j += 1;
            }
            i += 1;
        }
    }
}