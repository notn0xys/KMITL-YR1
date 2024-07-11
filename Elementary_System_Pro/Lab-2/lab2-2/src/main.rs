use std::io;
fn main() {
    let mut input = String::new();
    
    let mut employees: [(String,u32,f32);5] = [(String::new(), 0 , 0.0),(String::new(), 0 , 0.0),(String::new(), 0 , 0.0),(String::new(), 0 , 0.0),(String::new(), 0 , 0.0)];
    for i in 0..5{
        let emp = i + 1;
        println!("Enter Emplyee's {}'s Name: ", emp);
        io::stdin().read_line(&mut input).expect("Failed to read");
        employees[i].0 = input.trim().to_string();
        input.clear();
        println!("Enter Emplyee's {}'s Age: ", emp);
        io::stdin().read_line(&mut input).expect("Failed to read");
        employees[i].1 = input.trim().parse().expect("Invalid Age");
        input.clear();
        println!("Enter Emplyee's {}'s Salary: ", emp);
        io::stdin().read_line(&mut input).expect("Failed to read");
        employees[i].2 = input.trim().parse().expect("Invalid Salary");
        input.clear();
    }
    let mut highest:f32 = 0.0;
    let mut old = 0;
    let mut pay:f32 = 0.0;
    for i in 0..5{
        if highest < employees[i].2{
            highest = employees[i].2;
        }
        pay += employees[i].2;
        if old < employees[i].1{
            old = employees[i].1;
        }
        println!("Employee name = {:?}, Age = {:?}, Salary = {:?}", employees[i].0, employees[i].1,  employees[i].2);
    }
        for i in 0..5{
            if employees[i].2 == highest{
                println!("Employee with the highest salary is: {:?} with a salary of {:?}", employees[i].0 , employees[i].2);
            } 
            if employees[i].1 == old{
                println!("Oldest employee is: {:?} with an age of {:?}", employees[i].0 , employees[i].1);
    
            }
    
        }
    
    
}
