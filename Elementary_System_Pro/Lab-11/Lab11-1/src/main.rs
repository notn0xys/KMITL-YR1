struct Fibonacci{
    value:u32,
    last2:u32,
    last:u32,
    counter:u32
}
impl Iterator for  Fibonacci {
    type Item = u32;
    fn next(&mut self) -> Option<Self::Item> {
        if self.counter > 0 && self.counter < 3{
            if self.counter == 1{
                self.last = 1;
            }
        }
        else{
            self.last2 = self.last;
            self.last = self.value;
        }
        self.value = self.last + self.last2;
        self.counter += 1;
        Some(self.value)
    }
}
impl Fibonacci {
    fn new() -> Fibonacci{
        Fibonacci{value:0,last2: 0 ,last:0,counter:0}
    }
}
fn main() {
    let happy = Fibonacci::new();
    for (i,result) in happy.enumerate().take(20){
        println!("Fibonacci {}: {}",i + 1, result)
    }
}
