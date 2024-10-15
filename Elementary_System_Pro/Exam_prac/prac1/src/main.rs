use std::thread;
fn main() {
    let mut vec_of_threads = Vec::new();
    for i in 1..=5{
        let handle = thread::spawn(move || {
            let result = i * i;
            println!("Thread {i} {result}");
        });
        vec_of_threads.push(handle);
    }
    for threads in vec_of_threads{
        threads.join().unwrap();
    }
}
