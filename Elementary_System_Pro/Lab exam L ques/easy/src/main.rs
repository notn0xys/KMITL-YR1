use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;
fn main() {
    let args:Vec<String> = std::env::args().collect();
    let args = &args[1..];
    match args.len() {
        1 => {
            let file = match File::open(args[0].clone()) {
                Ok(file) => file,
                Err(e) => {
                    println!("{:?}",e);
                    std::process::exit(2)
                }
            };
            let reader = BufReader::new(file);
            let mut counter = 0;
            let mut vec_of_lines:Vec<_> = Vec::new();
            for i in reader.lines(){
                counter += 1;
                vec_of_lines.push(i.unwrap());
            }
            let mut words = 0;
            for i in vec_of_lines{
                let temp:Vec<&str>= i.split_whitespace().collect();
                words += temp.len();
            }
            println!("Lines {}",counter);
            println!("Words {}",words);
        }
        2 => {
            if args[1] == "-w"{
                let file = match File::open(args[0].clone()) {
                    Ok(file) => file,
                    Err(e) => {
                        println!("{:?}",e);
                        std::process::exit(2)
                    }
                };
                let reader = BufReader::new(file);
                let mut vec_of_lines:Vec<String> = Vec::new();
                for i in reader.lines(){
                    vec_of_lines.push(i.unwrap());
                }
                let mut words = 0;
                for i in vec_of_lines{
                    let temp:Vec<&str>= i.split_whitespace().collect();
                    words += temp.len();
                }
                println!("Words {}",words);
            }
            else if args[1] == "-l" {
                let file = match File::open(args[0].clone()) {
                    Ok(file) => file,
                    Err(e) => {
                        println!("{:?}",e);
                        std::process::exit(2)
                    }
                };
                let reader = BufReader::new(file);
                let mut counter = 0;
                for i in reader.lines(){
                    counter += 1;
                }
                println!("Lines {}",counter);
            }
            else {
                println!("Invalid Command");
                std::process::exit(2);
            }
        }
        _ => {
            println!("Invalid Argruments");
            std::process::exit(2);
        }
    }

}
