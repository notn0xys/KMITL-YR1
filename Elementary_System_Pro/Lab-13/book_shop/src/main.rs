mod library;
use library::{Library_Item, books::Book, media::AudioBook};

fn main() {
    let mut book = Book::new("Meow 🥺🥺🥺");
    let mut audio_book = AudioBook::new("Nyan :3");
    println!("{}",book.title());
    println!("{}",book.is_avaliable());
    book.check_out();
    println!("{}",book.is_avaliable());
    book.check_in();
    println!("{}",book.is_avaliable());
    println!("{}",audio_book.title());
    println!("{}",audio_book.is_avaliable());
    audio_book.check_out();
    println!("{}",audio_book.is_avaliable());
    audio_book.check_in();
    println!("{}",audio_book.is_avaliable());
    let library_items: Vec<&dyn Library_Item> = vec![&book, &audio_book];
    for i in library_items{
        println!("{}",i.title())
    }
}
