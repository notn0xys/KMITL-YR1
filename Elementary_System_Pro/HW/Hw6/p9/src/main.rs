struct Circle {
    radius:f32
}
impl Circle {
    fn new(x:f32) -> Self {
        Circle{radius:x}
    }
}

fn main() {
    let circle = Circle::new(10.0);
    println!("Circle with radius: {}", circle.radius);
}