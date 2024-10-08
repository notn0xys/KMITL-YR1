use std::thread;
use std::sync::mpsc;
fn main() {
    let (tx,rx) = mpsc::channel();
    println!("before block");
    let handle = thread::spawn(move || {
        let result = expensive_computation();
        tx.send(result).unwrap()
    });
    println!("everything before recv will run then stop to run");
    let result = rx.recv().unwrap();
    println!("Recieved {}",result);
    handle.join().unwrap();
    println!("AFTER BLOCK");
   
}
fn expensive_computation() -> i32{
    thread::sleep(std::time::Duration::from_secs(5));
    42
}
