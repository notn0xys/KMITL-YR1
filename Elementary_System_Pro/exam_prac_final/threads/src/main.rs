use std::thread;
fn main() {
    let mut number = 10;
    println!("{}", number);
    let handle = thread::spawn(move || {
        for i in 0..20{
            number += 1;
        }
        println!("Done");
    });
    handle.join().unwrap();
    println!("{}",number);
}
