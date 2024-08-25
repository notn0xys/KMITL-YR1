struct Person {
    name: String,
    age: i32
}

fn main() {
let nyah = Person {
    name: "meow".to_string(),
    age: 36
};
println!("{}", nyah.name);
println!("{}", nyah.age);

}
