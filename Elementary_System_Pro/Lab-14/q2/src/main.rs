use std::thread;
use std::sync::mpsc;

fn main() {
    let (tx, rx) = mpsc::channel();
    let handle = thread::spawn(move || {
        let mut num = 0;
        for i in 0..5{
            let count = count_nums(&mut num);
            tx.send(count).unwrap();
        }

    });
    for i in 0..5{
        let result = rx.recv().unwrap();
        println!("{}",result);
    }
    handle.join().unwrap();
}
fn count_nums(x: &mut i32) -> i32{
    *x += 1;
    thread::sleep(std::time::Duration::from_secs(1));
    *x
}