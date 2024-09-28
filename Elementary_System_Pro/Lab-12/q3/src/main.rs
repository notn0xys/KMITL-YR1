use std::path::Path;
use std::io::Read;
use std::ffi::OsStr;

fn main() {
    let args:Vec<_> = std::env::args().collect();
    let path = &args[1];
    let mut file_in = match std::fs::File::open(path) {
        Ok(val) => {val},
        Err(_) => {println!("File Not found");
        std::process::exit(2)},
    };
    let mut contents = String::new();
    match file_in.read_to_string(&mut contents) {
        Ok(num) => {num},
        Err(_) => {println!("Unable to read");
        std::process::exit(2)
        },
    };
    let lines = contents.lines().count();
    let words:Vec<_> = contents.split_whitespace().collect();
    let no_of_words = words.len();
    let name = OsStr::to_str(Path::new(path).file_name().unwrap()).unwrap();
    println!("Name: {}",name);
    println!("Lines: {}",lines);
    println!("Words: {}",no_of_words);
    println!("Characters: {}",contents.len());

    
}
