fn create_multiplier(factor: i32) -> impl Fn(i32) -> i32 {
    move |x| x * factor
}
fn main() {
    let a = "Hello".to_string(); // Variable to be moved
    let b = 20; // Variable to be borrowed

    // Create a closure that moves `a` but borrows `b`
    let closure = move || {
        // Use the moved variable `a`
        println!("Value of a inside closure: {}", a);
    };

    // Call the closure
    closure();

    // You can still use `b` here because it was borrowed, not moved
    println!("Value of a outside closure: {}", a);
}
