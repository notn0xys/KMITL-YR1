// fn add_one(x: &mut Vec<i32>) {
//     for i in  x{
//         *i += 1
//     }
// }
fn main() {
    let numbers = vec![1, 2, 3];
    let letters = vec!['a', 'b', 'c'];
    let pairs: Vec<(i32, char)> = numbers.iter().clone().zip(letters.iter()).collect();
}
