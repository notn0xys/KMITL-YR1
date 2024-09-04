fn main() {
    let mut r:Vec<i32> = Vec::new();
    println!("Initial L {} and Initial C {}" , r.len(),r.capacity());
    for i in 0..5{
        r.push(i);
    }
    println!("New L {} and New C {}" , r.len(),r.capacity());
    let mut new_vec:Vec<i32> = Vec::with_capacity(10);
    for i in 0..15{
        new_vec.push(i);
    }
    println!("NewVec L {} and NewVec C {}" , new_vec.len(),new_vec.capacity());

}
