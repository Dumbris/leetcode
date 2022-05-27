use std::collections::HashSet;    

pub fn sum_digits(n: i32) -> i32 {
        let mut num = n;
        let base = 10usize;
        let mut digit = 0;
        let mut sum = 0;
        while num != 0 {
            //println!("{:?}", num % base as i32);
            sum = sum + i32::pow(num % base as i32, 2);
            num /= base as i32;
            digit += 1;
        }
        //println!("{:?}", sum);
        sum
    }

impl Solution {
    pub fn is_happy(n: i32) -> bool {
        let mut res:i32 = n;
        let mut seen = HashSet::new();
        seen.insert(n);
        let x = loop {
            res = sum_digits(res);
            if res == 1 {
                break true
            }
            if seen.contains(&res) {
                break false
            }
            seen.insert(res);           
            
        };
        x
    }
}