use std::result;

fn swap_result<T1,T2>(a:Vec<T1>,b:Vec<T2>) -> (Vec<T2>,Vec<T1>) {
    return (b,a);
}


fn main() {
    let vec1 = vec![1,2,3];
    let vec2 = vec!["meow","nyah", "gayass"];
    let result = swap_result(vec1, vec2);
    println!("{:?} , {:?}",result.0, result.1);
}
