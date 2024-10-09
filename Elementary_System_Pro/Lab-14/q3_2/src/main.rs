use std::thread;
use std::sync::mpsc;
use rand::Rng;
use std::time::{Duration, Instant};


fn main() {
    let start: Instant = Instant::now();
    let (tx, rx) = mpsc::channel();
    let list_of_nums:Vec<u32> = (0..1_000_000).map(|_| rand::thread_rng().gen_range(1..=100)).collect();
    let handle = thread::spawn(move || {
        let result = calc(&list_of_nums);
        tx.send(result).unwrap();
    });
    let result = rx.recv().unwrap();
    println!("{}",result);
    handle.join().unwrap();
    let duration = start.elapsed();
    println!("Time elapsed  is: {:?}", duration);
}
fn calc(x:&[u32]) -> u32{
    let mut result = 0;
    for i in x{
        result += i * i;
    }
    result
}
