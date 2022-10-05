use std::collections::HashSet;
use std::iter::FromIterator;

impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        let mut hs:HashSet<i32> = HashSet::from_iter(nums);
        if hs.contains(&0) {
            (hs.len() - 1) as i32    
        } else {
            hs.len() as i32
        }
        
    }
}
