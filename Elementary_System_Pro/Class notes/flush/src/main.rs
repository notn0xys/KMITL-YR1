use std::io::{self,Write};

fn main() {
    let mut stdout = io::stdout();
    stdout.write(b"Hello nigga").unwrap();
    stdout.flush().unwrap()
   
}
