use std::mem::*;
struct Point{
    x:i32,
    y:i32
}

enum Shape {
    Circle {point:Point, radius:f32},
    Rectangle {top_left:Point, bottom_right:Point}
}

fn main() {
    println!("{}", size_of::<Point>());
    println!("{}", size_of::<Shape>());
    println!("Size of Circle Varient {} ", size_of::<Shape>());
    println!("Size of Rectangle Varient {}", size_of::<Shape>());
}
