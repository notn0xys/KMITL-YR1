struct Rectangle {
    width:i32,
    height:i32
}
impl Rectangle {
    fn area(&self) -> i32 {
        return self.width * self.height;
    }
}

fn main() {
    let rect = Rectangle { width: 10, height: 20 };
    println!("Area: {}", rect.area());
}