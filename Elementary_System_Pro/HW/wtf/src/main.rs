fn find_longest_word(x:&str) -> &str {
    let y = x.split_whitespace();
    let mut z = "";
    for i in y{
        if i.len() >= z.len(){
            z = i;
        }
    }
    z
}


fn main() {
    let sentence = "The quick brown fox jumps over the lazy dog";
    let longest = find_longest_word(sentence);
    println!("The longest word is: {}", longest); // jumps 
}     