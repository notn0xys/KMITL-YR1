struct Colors {
    rbg:(u8,u8,u8)
}

fn main() {
    let new_col = Colors{
        rbg:(28,28,23)
    };
    println!("{:?}", new_col.rbg);
}
