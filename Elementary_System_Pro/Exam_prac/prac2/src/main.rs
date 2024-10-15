fn main() {
    let args: Vec<_> = std::env::args().collect();
    if args.len() != 4{
        let meow = args.len() - 1;
        println!("This program takes 3 argruments you provided {}",meow);
        std::process::exit(0);
    }
    else{
        println!("You provided {}, {}, {} ",args[1],args[2],args[3]);
        std::process::exit(0);
    }
}

