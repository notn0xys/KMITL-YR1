use std::io::{self, Read, Write};
fn main() {
    let mut need_write: String = String::new();
    loop{
        println!("Enter Contents: ");
        let mut input: String = "".to_string();
        match io::stdin().read_line(&mut input) {
            Ok(val) => val,
            Err(_) => {continue;},
        };
        if input == "\r\n"{
            break;
        }

        need_write.push_str(&input);

    }
    let mut file = std::fs::File::create("data.txt").unwrap();
    file.write_all(need_write.as_bytes()).unwrap();
    let mut file = std::fs::File::open("data.txt").unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    print!("Contents: {}", contents.to_uppercase());
}
