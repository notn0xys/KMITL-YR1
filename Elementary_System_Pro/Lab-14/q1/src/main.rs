use std::thread;
fn main() {
    let mut new = Vec::new();
    for i in 1..=5{
        let handle = thread::spawn(move || {println!("Thread {} Result {} ",i,i*i);
        });
        new.push(handle);
    }
    for handle in new{
        handle.join().unwrap();
    }

}
