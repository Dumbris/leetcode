impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let s2:String = s.to_ascii_lowercase().chars().filter(|&x| x.is_ascii_alphanumeric()).collect();
        if s2.len() == 0 {
            return true;
        }
        let mut i:usize = 0;
        let mut j:usize = s2.len()-1;
        let my_vec: Vec<char> = s2.chars().collect();
    while i < j {
      if my_vec[i] != my_vec[j] {
        return false;
      }
      i += 1;
      j -= 1;
    }
    return true;
    }
}