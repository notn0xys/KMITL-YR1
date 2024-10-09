use std::thread;
use std::sync::mpsc;
use rand::Rng;
use std::time::{Duration, Instant};
fn main() {
    let start: Instant = Instant::now();
    let mut new = Vec::new();
    let (tx, rx) = mpsc::channel();
    let list_of_nums:Vec<u32> = (0..1_000_000).map(|_| rand::thread_rng().gen_range(1..=100)).collect();
    for chunk in list_of_nums.chunks(100000) {
        let chunk = chunk.to_vec();
        let tx= tx.clone();
        let handle = thread::spawn(move || {
            let result = calc(&chunk);
            tx.send(result).unwrap();
        });
        new.push(handle);   
    }
    let mut total: u32 = 0;
    for i in 0..10{
        let result = rx.recv().unwrap();
        total += result;
    }
    let duration = start.elapsed();
    println!("Time elapsed  is: {:?}", duration);
    for i in new{
        i.join().unwrap()
    }
    println!("{}",total);
}
fn calc(x:&[u32]) -> u32{
    let mut result = 0;
    for i in x{
        result += i * i;
    }
    result
}
