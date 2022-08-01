use std::collections::HashMap;
/////////Leetcode
#[derive(Default)]
struct Trie {
    child: HashMap<char, Box<Trie>>,
    is_terminal: bool,

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Trie {

    fn new() -> Self {
        Default::default()
        
    }
    
    fn insert(&mut self, word: String) {
        let mut p = self;
        for c in word.chars() {
            p = p.child.entry(c).or_insert(Default::default());
        }
        p.is_terminal = true;
    }
    
    fn search(&self, word: String) -> bool {
        let mut p = self;
        for c in word.chars() {
            if let Some(next) = p.child.get(&c) {
                p = next;
            } else {
                return false;
            }
        }
        p.is_terminal
    }
    
    fn starts_with(&self, prefix: String) -> bool {
        let mut p = self;
        for c in prefix.chars() {
            if let Some(next) = p.child.get(&c) {
                p = next;
            } else {
                return false;
            }
        }
        true
    }
}