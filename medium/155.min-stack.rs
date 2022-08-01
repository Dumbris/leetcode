#[derive(Default)]
struct MinStack {
    stack: Vec<i32>,
    min: Vec<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MinStack {

    fn new() -> Self {
        Default::default()
    }
    
    fn push(&mut self, val: i32) {
        if self.stack.is_empty() || val < self.get_min() {
            self.min.push(val); 
        } else { 
            self.min.push(self.get_min()); 
        }
        self.stack.push(val);
    }
    
    fn pop(&mut self) {
        self.stack.pop();
        self.min.pop();
    }
    
    fn top(&self) -> i32 {
        *self.stack.last().unwrap()
    }
    
    fn get_min(&self) -> i32 {
        //println!("{:?}", (self.stack.to_owned(), self.min.to_owned()));
        *self.min.last().unwrap()
    }
}