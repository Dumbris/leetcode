impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let mut j = 0;
        for i in nums {
            j ^= i;
        }
        j
            
    }
    pub fn single_number2(nums: Vec<i32>) -> i32 {
        nums.into_iter().fold(0, |acc, x| acc ^ x) 
    }
}

