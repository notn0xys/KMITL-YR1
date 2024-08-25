fn calculate(x:i32,y:i32) -> (i32,i32) {
    let z = x + y;
    let m = x * y;
    let new:(i32,i32) = (z,m);
    return new;
}
fn main() {
    let result = calculate(3, 4);
    println!("Sum: {}, Product: {}", result.0, result.1);
}
