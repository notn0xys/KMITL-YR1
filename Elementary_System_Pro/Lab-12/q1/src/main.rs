
fn main() {
    let args:Vec<_> = std::env::args().collect();
    if args.len() != 4{
        let meow = args.len() - 1;
        println!("Error: Excatly 3 argrument required. You Provided {meow}");
        std::process::exit(2)
    }
    else{
       println!("Argrument Porvided {} {} {}",args[1],args[2],args[3]);
       std::process::exit(0)
    }
    
}
