fn main() {
    let temp: Vec<i32> = vec![-3, 4, -1, 5, -7];
    let max_val:i32 = temp.iter()
        .filter(|&x| *x = 0)
        .map(|&x| x)
        .sum();
    println!("{}", max_val); // Output: [4, 5]
}

// fn main() {
//     let numbers = vec![1, 2, 3, 4, 5, 6];
    
//     let result: i32 = numbers
//     .iter() // Create an iterator
//     .filter(|&x| x % 2 == 0) // Filter even numbers
//     .map(|&x| x * x) // Square each even number
//     .sum(); // Sum the results
    
//     println!("The sum of squares of even numbers is: {}", result);
// }