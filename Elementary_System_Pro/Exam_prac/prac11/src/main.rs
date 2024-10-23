use std::thread;
fn main() {
    let mut vec_handle = Vec::new();
    for i in 1..=5{
        let handle = thread::spawn(move || { println!("Thread {} result {}" , i, i*i)});
        vec_handle.push(handle);
    }
    for handle in vec_handle{
        handle.join().unwrap();
    }
}   
