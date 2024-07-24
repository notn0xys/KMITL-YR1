use std::io;

fn pascal(i:i32, j:i32) -> i32{
    if j == 0{
        1
    }else if j == i {
        1
    }else {
        let a =  pascal(i-1, j-1) + pascal(i-1, j);
        a
    }
}

fn row_pascal(x:i32, y:i32 ) {
    let a = pascal(x, y);
    print!("{:<4}", a);
}




fn main() {
    let row:i32 = loop {
        let mut input = String::new();
        println!("Enter the amount of Rows: ");
        io::stdin().read_line(&mut input).expect("Failed to read");
        match input.trim().parse() {
            Ok(num) if (1..=9).contains(&num) => break num,
            _ => println!("Enter a valid number"),
        }
    };
    for i in 0..row{
        for k in 0..((row - i ) * 2)- 2{
            print!(" ");
        }
        for j in 0..i+1{
            row_pascal(i, j)
            
        }

        println!("")
    }
}
