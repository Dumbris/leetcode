use std::cmp::max;
use std::collections::HashSet;
impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let (mut l, mut max_len) = (0, 0);
        let mut hs = HashSet::new();
        let chars:Vec<_> = s.chars().collect();
        for (i, c) in chars.iter().enumerate() {
            while hs.contains(&c) {
                hs.remove(&chars[l]);
                l += 1;
            }
            hs.insert(c);
            max_len = max(max_len, hs.len());
        }
        max_len as i32
    }
}