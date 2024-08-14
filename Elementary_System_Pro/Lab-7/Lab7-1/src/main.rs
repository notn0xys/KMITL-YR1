fn fac(x:i32) -> i32{
    println!("Calculating Factorial {}",x);
    println!("Value {}, Memory Adress {:p} ",x,&x);
    if x == 1{
        1
    }
    else{
        let a = x * fac(x - 1);
        a
    }
}

fn main(){
    let a = fac(5);
    println!("Factorial Result: {a}");
}
