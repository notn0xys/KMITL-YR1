use core::num;
use std::{io, u32};

fn main() {
    let mut data: Vec<(u32, String, u32)> = Vec::new();


    loop {
        println!("Inventory Management system");
        println!("1) Add a new Product");
        println!("2) Update Stock Quantity");
        println!("3) Remove Product ");
        println!("4) List all Products");
        println!("5) Exit ");


        let mut choicde = String::new();
        io::stdin().read_line(&mut choicde).expect("Failed to read line");
        let choice:i8 = match choicde.trim().parse(){
            Ok(num) => num,
            Err(_) =>{
                println!("Invalid Input");
                continue;
            }
        };
        if choice ==  1{
            let mut id_exist = false;
            let mut input = String::new();
            println!("Enter amount of Items You wish to add");
            io::stdin().read_line(&mut input).expect("Failed to read line");
            let amount:u32 = match input.trim().parse(){
                Ok(num)=> num,
                Err(_) =>{
                    println!("Invalid Input type");
                    continue;
                }

            };
            input.clear();
            println!("Enter The item name");
            io::stdin().read_line(&mut input).expect("Failed to read line");
            let name: String = input.trim().to_string();
            input.clear();
            println!("Enter Item ID");
            io::stdin().read_line(&mut input).expect("Failed to read line");
            let id:u32 = match input.trim().parse(){
                Ok(num)=> num,
                Err(_) =>{
                    println!("Invalid Input type");
                    continue;
                }

            };
            input.clear();
            for i in &data{
                if id == i.0{
                    id_exist = true;
                    break;
                }
            }
            if id_exist == true{
                println!("ID already exist ");
                continue;
            }else {
                data.push((id, name ,amount));
            }

        }else if choice == 2 {
            let mut input = String::new();
            let mut id_exist = false;
            println!("Enter The Product ID you wish to update quantity");
            io::stdin().read_line(&mut input).expect("Failed to read line");
            let id:u32 = match input.trim().parse(){
                Ok(num) => num,
                Err(_) =>{
                    println!("Invalid Input");
                    continue;
                }
            };
            input.clear();
            println!("Enter The Amount you want to change it to");
            io::stdin().read_line(&mut input).expect("Failed to read line");
            let amount:u32 = match input.trim().parse(){
                Ok(num) => num,
                Err(_) =>{
                    println!("Invalid Input");
                    continue;
                }
            };
            for i in &data{
                if id == i.0{
                    id_exist = true;
                    break;
                }
            }
            if id_exist == true{
                for j in 0..data.len(){
                    if id == data[j].0{
                        data[j].2 = amount;
                    }
                }
                    continue;
            } else {
                println!("ID Not found");
                continue;
            }
        }else if  choice == 3 { 
            let mut input = String::new();
            let mut id_exist = false;
            println!("Enter The Product ID you wish to remove");
            io::stdin().read_line(&mut input).expect("Failed to read line");
            let id:u32 = match input.trim().parse(){
                Ok(num) => num,
                Err(_) =>{
                    println!("Invalid Input wtf");
                    continue;
                }
            };
            for i in &data{
                if id == i.0{
                    id_exist = true;
                    break;
                }
            }
            if id_exist == true{
                for j in 0..data.len(){
                    if id == data[j].0{
                        data.remove(j);
                        println!("Item Removed");
                    }
                }
                continue;
            }else {
                println!("ID Not found");
                continue;
            }


        }else if  choice == 4 {
            for i in 0..data.len(){
                println!("Product ID: {} Product name: {} Amount of Product: {} ",data[i].0 , data[i].1 , data[i].2);
            }
        }else if choice ==5 {
            println!("Exiting Program");
            break;
        }else {
            println!("Invalid Choice: ");
            continue;
        }
    }



}
