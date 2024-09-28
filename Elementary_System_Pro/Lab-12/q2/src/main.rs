
fn main() {
    let args:Vec<_> = std::env::args().collect();
    if args.len() != 4{
        println!("Missing arguments");
        std::process::exit(2)
    }   
    else{
        let num1:i32 = args[1].parse().expect("Not an integer");
        let num2:i32 = args[3].parse().expect("Not an integer");
        let op = args[2].clone();
        let op_str = &*op;
        match op_str {
            "+"  => {
                println!("Result: {} ", num1 + num2)
            }
            "-" => {
                println!("Result: {} ", num1 - num2) 
            }
            "*" => {
                println!("Result: {} ", num1 * num2)
            }
            "/"  => {
                if num2 != 0{
                    println!("Result: {} ", num1 / num2)
                }
                else {
                    println!("Cant divide by 0");
                    std::process::exit(2)
                }
            }
            _ => {
                println!("Unsupported operators");
                std::process::exit(2)
            }            
        }
    }
}
