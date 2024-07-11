use std::io;

fn main() {
    let mut name1 = String::new();
    let mut name2 = String::new();
    println!("Type your first name: ");
    io::stdin().read_line(&mut name1).expect("Failed to read");
    println!("Type your Second name: ");
    io::stdin().read_line(&mut name2).expect("Failed to read");
    name1 = name1.trim().to_string();
    name2 = name2.trim().to_string();
    let mut name1_lenght = name1.len();
    let name2_lenght = name2.len();

    while name1_lenght < name2_lenght{
        name1_lenght += 1;
        if name1_lenght == name2_lenght{
            break;
        }
    }
    let total = name1_lenght + 12;

    for i in 0..9{
        if i == 0 || i == 4 || i == 8 {
            print!("*");
            for j in 0..total{
                print!("*");
            }
            println!("*");
        }
    
        if i == 1 || i == 3 || i ==5 || i ==7{
            print!("*");
            for j in 0..total{
                print!(" ");
            }
            println!("*");
        }
        if i == 2{
            print!("*");
            print!(" Player 1: {} ", name1);
            let space_to_add = name1_lenght - name1.len();
            for i in 0..space_to_add{
                print!(" ")
            }
            println!("*");
        }
        if i == 6{
            print!("*");
            print!(" Player 2: {} ", name2);
            let space_to_add = name1_lenght - name2.len();
            for i in 0..space_to_add{
                print!(" ")
            }
            println!("*");
        }
    }

    let horizontal_l = name1.len() + name2.len() + 25;
    let middle_part = 12 + name1.len();
    for i in 0..5{
        if i == 0 || i == 4{
            print!("*");
            for j in 0.. horizontal_l{
             print!("*");   
            }
            println!("*");


        }
        if i == 1 || i == 3{
            print!("*");
            for j in 0..horizontal_l-1{
                print!(" ");
                if j == (middle_part- 1){
                    print!("*");
                }
            }
            println!("*");
        }
        if i ==2{
            for j in 0..horizontal_l{
                if j == 0{
                    print!("*");
                }
                if j == 1{
                    print!(" Player 1: {} ", name1);
                }
                if j == middle_part - 1{
                    print!("*");
                    print!(" Player 2: {} ", name2);
                    println!("*")
                    

                }



            }
            
        }
        
    }

}
