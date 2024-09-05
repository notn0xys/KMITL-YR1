
struct Data {
    num:i32,
    character:char,
    boool:bool,
}
fn view<T>(o: &T) -> &[u8] {
    unsafe {
    std::slice::from_raw_parts( // creates a byte slice from a raw pointer (*const u8) and a length
    o as *const _ as *const u8, // converts into a raw pointer of type *const u8
    std::mem::size_of::<T>() // calculates the size of the object in bytes
    )
    }
}
fn main() {
    let data: Data = Data {
        num:65280,
        character:'f',
        boool:true
    };
    println!("{:?}", view(&data));

}
