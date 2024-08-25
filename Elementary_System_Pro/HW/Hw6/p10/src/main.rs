struct book {
    title:String,
    author:String,
    published_year:Option<u32>
}

fn main() {
    let meow = book{
        title:"Noxy adventure".to_string(),
        author:"Rizz".to_string(),
        published_year:None
    };
    match meow.published_year {
        Some(year) => println!("{} was published in {}", meow.title, year),
        None => println!("{} has no publication year", meow.title),
    }
}