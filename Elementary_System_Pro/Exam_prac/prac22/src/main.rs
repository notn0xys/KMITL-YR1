fn main() {
    let args:Vec<_> = std::env::args().collect();
    if args.len() != 4{
        println!("3 Argrument required you provided {} ", args.len() - 1);
        std::process::exit(2);
    }
    else{
        println!("Argruments Provided {}, {}, {} ", args[1],args[2],args[3]);
        std::process::exit(0);
    }
}
