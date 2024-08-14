use core::num;

struct BoxedStack{
    data:Box<Vec<i32>>,
    meow:Box<Vec<i32>>
}

impl BoxedStack {
    fn new() -> Self{
        BoxedStack{data:Box::new(vec![]),meow:Box::new(vec![])}

    }
    fn push(&mut self, value:i32) {
        println!("Pushing {} to the stack",value);
        (*self.data).push(value);
    }
    fn pop(&mut self) -> Option<i32>{
        if (*self.data).is_empty(){
            println!("Nothing left in the stack");
            return None;
        }
        else{
            println!("Removed Top of the stack");
            (*self.data).pop()

        }
    }
    fn peek(&mut self) -> Option<&i32>{
        let lenght = (*self.data).len() - 1;
        if !(*self.data).is_empty(){
            Some(&(*self.data)[lenght])
        }
        else{
            None
        }
    }
    fn is_empty(&self) -> bool {
        (*self.data).is_empty()
    }
    fn print_stack(&self) {
        println!("{:?}",*self.data);
    }
}

fn main() {
    let mut nyah = BoxedStack::new();
    nyah.push(10);
    nyah.push(20);
    nyah.push(30);
    nyah.print_stack();
    let a = nyah.pop();
    match a {
        Some(num) => {
            println!("Popped {num} out of the stack");
        }
        None => println!("Nothing left in the stack"),
    }
    nyah.push(10);
    nyah.print_stack();
    let a = nyah.pop();
    match a {
        Some(num) => {
            println!("Popped {num} out of the stack");
        }
        None => println!("Nothing left in the stack"),
    }
    nyah.print_stack();
    let b = nyah.peek();
    match b {
        Some(num) => {
            println!("{}", num);
        }
        None => println!("Nothing left in the stack"),
    }

    
}
