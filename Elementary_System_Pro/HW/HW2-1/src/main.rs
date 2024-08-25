fn get_substring (x:&String,y:usize,z:usize) -> &str{
    match x.get(y..z) {
        Some(txt) => txt,
        None => {
            let meow = "Doesnt exist";
            meow
        }
    }
}


fn main() {
    let s = String::from("Hello, World!");
    let result = get_substring(&s, 7, 12);
    println!("{}", result); // World
}