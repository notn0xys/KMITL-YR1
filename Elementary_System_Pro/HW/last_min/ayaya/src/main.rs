fn find_longest_word(x:&str) -> String {
    let y = x.split_whitespace();
    let mut nigga = "";
    for i in y{
        if i.len() >= nigga.len(){
            nigga = i;
        }

    }
    nigga.to_string()
}

fn main() {
    let sentence = "The quick brown fox jumps over the lazy dog";
    let longest = find_longest_word(sentence);
    println!("The longest word is: {}", longest); // jumps
}